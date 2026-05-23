import os
from typing import List
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('NOVALIKE_API_TOKEN', '')

app = FastAPI(
    title='NovaLike API',
    version='0.3.0',
    description='API communautaire NovaLike'
)

message_queue: List[dict] = []


class DiscordMessage(BaseModel):
    author: str
    content: str
    channel: str | None = None
    channel_id: int | None = None
    guild: str | None = None
    roles: list[str] = []
    mentioned: bool = False


class GPTMessage(BaseModel):
    message: str
    channel_id: int | None = None


@app.get('/health')
async def health():
    return {
        'name': 'NovaLike API',
        'status': 'online',
        'queue_size': len(message_queue)
    }


def normalize(value: str | None) -> str:
    return (value or '').lower().strip()


def has_unverified_role(roles: list[str]) -> bool:
    normalized = [normalize(role).replace('-', ' ') for role in roles]
    return any(role in normalized for role in ['unverified', 'non verifie', 'non verifiee'])


def should_reply(payload: DiscordMessage) -> bool:
    content = normalize(payload.content)
    channel = normalize(payload.channel)

    if payload.mentioned:
        return True

    if content.startswith('nova') or content.startswith('novalike'):
        return True

    if 'accueil' in channel and has_unverified_role(payload.roles):
        return True

    if 'reglement' in channel or 'règlement' in channel:
        return True

    if 'je vois pas' in content or 'pas les salons' in content or 'pas acces' in content or 'pas accès' in content:
        return True

    return False


def contextual_reply(payload: DiscordMessage) -> str:
    content = normalize(payload.content)
    channel = normalize(payload.channel)
    unverified = has_unverified_role(payload.roles)

    if unverified or 'pas les salons' in content or 'pas acces' in content or 'pas accès' in content:
        return "👋 Bienvenue ! Pour débloquer tous les salons, va dans #📜・règlement puis clique sur le logo WanaLike en bas du règlement. Après validation, tu verras le reste du serveur."

    if 'reglement' in channel or 'règlement' in channel:
        return "Pour valider ton accès, lis le règlement puis clique sur le logo WanaLike en bas du message. C’est ce qui débloque les autres salons 🙂"

    if 'radio' in channel:
        return "🎧 Bienvenue côté WanaFM ! Tu peux discuter musique, demander des sons ou suivre ce qui passe sur la radio."

    if 'suggestions' in channel:
        return "💡 Bonne idée. Si tu peux, détaille le besoin, l’objectif et l’impact attendu : ça aidera le staff à trier proprement."

    if 'accueil' in channel:
        return "👋 Bienvenue sur WanaLike ! Tu viens plutôt pour la radio, le dev, le gaming ou juste chiller ?"

    return "👋 Je suis NovaLike. Je peux t’aider à te repérer, t’orienter vers les bons salons ou relancer la discussion."


@app.post('/discord/message')
async def discord_message(payload: DiscordMessage):
    if not should_reply(payload):
        return {
            'should_reply': False,
            'reply': ''
        }

    return {
        'should_reply': True,
        'reply': contextual_reply(payload)
    }


@app.post('/gpt/send-message')
async def gpt_send_message(
    payload: GPTMessage,
    x_api_token: str = Header(default='')
):
    if x_api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail='Invalid API token')

    message_queue.append({
        'message': payload.message,
        'channel_id': payload.channel_id
    })

    return {
        'status': 'queued',
        'message': payload.message,
        'queue_size': len(message_queue)
    }


@app.get('/bot/pending-messages')
async def bot_pending_messages(
    x_api_token: str = Header(default='')
):
    if x_api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail='Invalid API token')

    messages = message_queue.copy()
    message_queue.clear()

    return {
        'messages': messages,
        'count': len(messages)
    }

import os
import random
from typing import List
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('NOVALIKE_API_TOKEN', '')
WANALIKE_MARK = chr(60) + ':wanalike:1443556453918048276' + chr(62)

app = FastAPI(
    title='NovaLike API',
    version='0.3.2',
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


class GPTPublicMessage(BaseModel):
    token: str
    message: str
    channel_id: int | None = None


@app.get('/health')
async def health():
    return {'name': 'NovaLike API', 'status': 'online', 'queue_size': len(message_queue)}


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
    if 'salut' in content or 'hello' in content or 'coucou' in content:
        return payload.mentioned or content.startswith(('nova', 'novalike'))
    return False


def pick(items: list[str]) -> str:
    return random.choice(items)


def contextual_reply(payload: DiscordMessage) -> str:
    content = normalize(payload.content)
    channel = normalize(payload.channel)
    unverified = has_unverified_role(payload.roles)

    if unverified or 'pas les salons' in content or 'pas acces' in content or 'pas accès' in content:
        return pick([
            f"Yes, t'es juste pas encore validé 🙂 Va dans #📜・règlement et clique sur {WANALIKE_MARK} en bas du règlement. Après ça, les salons se débloquent.",
            f"Pas de panique 👋 Pour voir tous les salons, passe dans #📜・règlement puis clique sur {WANALIKE_MARK} en bas du message.",
            f"Il te manque sûrement la validation. Direction #📜・règlement, clique sur {WANALIKE_MARK}, et tu devrais voir le reste du serveur."
        ])

    if 'reglement' in channel or 'règlement' in channel:
        return pick([
            f"Pour valider ton accès, lis le règlement puis clique sur {WANALIKE_MARK} en bas du message 🙂",
            f"La validation se fait ici : tu lis le règlement, puis tu cliques sur {WANALIKE_MARK}. Après ça, les salons s’ouvrent.",
        ])

    if 'radio' in channel:
        return pick([
            '🎧 Bienvenue côté WanaFM ! Ici ça parle sons, ambiance, demandes et découvertes.',
            '🎶 Coin radio ici. Tu peux parler musique, proposer des sons ou suivre ce qui passe sur WanaFM.',
        ])

    if 'suggestions' in channel:
        return '💡 Bonne idée. Décris le besoin, l’objectif et l’impact attendu : ça aidera le staff à trier proprement.'

    if 'accueil' in channel:
        return pick([
            'Hey 👋 Bienvenue sur WanaLike ! Tu viens plutôt pour la radio, le dev, le gaming ou juste chiller ?',
            'Bienvenue ici 👋 Installe-toi tranquille. Tu viens découvrir quel coin du serveur ?',
            'Salut 👋 Ravi de te voir passer. Si tu cherches un salon précis, je peux t’orienter.',
        ])

    return 'Je suis là 👋 Je peux t’aider à te repérer, trouver le bon salon ou relancer un peu la discussion.'


@app.post('/discord/message')
async def discord_message(payload: DiscordMessage):
    if not should_reply(payload):
        return {'should_reply': False, 'reply': ''}
    return {'should_reply': True, 'reply': contextual_reply(payload)}


@app.post('/gpt/send-message')
async def gpt_send_message(payload: GPTMessage, x_api_token: str = Header(default=''), authorization: str = Header(default='')):
    bearer = ''
    if authorization.lower().startswith('bearer '):
        bearer = authorization.split(' ', 1)[1].strip()
    if x_api_token.strip() != API_TOKEN.strip() and bearer != API_TOKEN.strip():
        raise HTTPException(status_code=401, detail='Invalid API token')
    message_queue.append({'message': payload.message, 'channel_id': payload.channel_id})
    return {'status': 'queued', 'message': payload.message, 'queue_size': len(message_queue)}


@app.post('/gpt/send-message-public')
async def gpt_send_message_public(payload: GPTPublicMessage):
    if payload.token.strip() != API_TOKEN.strip():
        raise HTTPException(status_code=401, detail='Invalid API token')
    message_queue.append({'message': payload.message, 'channel_id': payload.channel_id})
    return {'status': 'queued', 'message': payload.message, 'queue_size': len(message_queue)}


@app.get('/bot/pending-messages')
async def bot_pending_messages(x_api_token: str = Header(default=''), authorization: str = Header(default='')):
    bearer = ''
    if authorization.lower().startswith('bearer '):
        bearer = authorization.split(' ', 1)[1].strip()
    if x_api_token.strip() != API_TOKEN.strip() and bearer != API_TOKEN.strip():
        raise HTTPException(status_code=401, detail='Invalid API token')
    messages = message_queue.copy()
    message_queue.clear()
    return {'messages': messages, 'count': len(messages)}

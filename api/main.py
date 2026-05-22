import os
from typing import List
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('NOVALIKE_API_TOKEN', '')

app = FastAPI(
    title='NovaLike API',
    version='0.2.0',
    description='API communautaire NovaLike'
)

message_queue: List[dict] = []


class DiscordMessage(BaseModel):
    author: str
    content: str
    channel: str | None = None


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


@app.post('/discord/message')
async def discord_message(payload: DiscordMessage):
    return {
        'reply': f'👋 Salut {payload.author}, NovaLike a reçu : {payload.content}'
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

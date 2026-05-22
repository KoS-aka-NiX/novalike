import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title='NovaLike API',
    version='0.1.0',
    description='API communautaire NovaLike'
)


class DiscordMessage(BaseModel):
    author: str
    content: str
    channel: str | None = None


class GPTMessage(BaseModel):
    message: str


@app.get('/health')
async def health():
    return {
        'name': 'NovaLike API',
        'status': 'online'
    }


@app.post('/discord/message')
async def discord_message(payload: DiscordMessage):
    return {
        'reply': f'NovaLike a reçu le message de {payload.author}: {payload.content}'
    }


@app.post('/gpt/send-message')
async def gpt_send_message(payload: GPTMessage):
    return {
        'status': 'ok',
        'message': payload.message
    }

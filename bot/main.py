import os
import asyncio
import discord
import httpx
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX', '!')
STATUS = os.getenv('BOT_STATUS', 'NovaLike is online')
API_BASE_URL = os.getenv('API_BASE_URL', 'http://127.0.0.1:8000')
API_TOKEN = os.getenv('NOVALIKE_API_TOKEN', '')
DEFAULT_CHANNEL_ID = os.getenv('DISCORD_DEFAULT_CHANNEL_ID')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


async def poll_api_messages():
    await bot.wait_until_ready()

    while not bot.is_closed():
        try:
            async with httpx.AsyncClient(timeout=15) as client:
                response = await client.get(
                    f'{API_BASE_URL}/bot/pending-messages',
                    headers={
                        'X-API-Token': API_TOKEN
                    }
                )

                data = response.json()

                for item in data.get('messages', []):
                    channel_id = item.get('channel_id') or DEFAULT_CHANNEL_ID

                    if not channel_id:
                        continue

                    channel = bot.get_channel(int(channel_id))

                    if channel:
                        await channel.send(item.get('message', '👋'))

        except Exception as e:
            print(f'[NovaLike] Polling error: {e}')

        await asyncio.sleep(5)


@bot.event
async def on_ready():
    print(f'[NovaLike] Connected as {bot.user}')

    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name=STATUS
    )

    await bot.change_presence(activity=activity)

    bot.loop.create_task(poll_api_messages())


@bot.event
async def on_member_join(member):
    print(f'[NovaLike] New member joined: {member.name}')

    try:
        if member.guild.system_channel:
            await member.guild.system_channel.send(
                f'👋 Bienvenue {member.mention} sur **{member.guild.name}** !'
            )
    except Exception as e:
        print(f'[NovaLike] Welcome message failed: {e}')


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(
                f'{API_BASE_URL}/discord/message',
                json={
                    'author': str(message.author),
                    'content': message.content,
                    'channel': str(message.channel)
                }
            )

            data = response.json()

            if message.content.lower().startswith('nova'):
                await message.channel.send(data.get('reply', '👋'))

    except Exception as e:
        print(f'[NovaLike] API error: {e}')

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'🏓 Pong ! `{latency}ms`')


@bot.command()
async def nova(ctx):
    await ctx.send('👋 Salut, je suis NovaLike, l’IA communautaire WanaLike.')


bot.run(TOKEN)

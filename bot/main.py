import os
import discord
import httpx
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX', '!')
STATUS = os.getenv('BOT_STATUS', 'NovaLike is online')
API_BASE_URL = os.getenv('API_BASE_URL', 'http://127.0.0.1:8000')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    print(f'[NovaLike] Connected as {bot.user}')

    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name=STATUS
    )

    await bot.change_presence(activity=activity)


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

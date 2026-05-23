import os
import asyncio
import logging
import discord
import httpx
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s'
)

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX', '!')
STATUS = os.getenv('BOT_STATUS', 'NovaLike is online')
API_BASE_URL = os.getenv('API_BASE_URL', 'http://127.0.0.1:9010')
API_TOKEN = os.getenv('NOVALIKE_API_TOKEN', '')
DEFAULT_CHANNEL_ID = os.getenv('DISCORD_DEFAULT_CHANNEL_ID')
AI_TESTER_ROLE = os.getenv('NOVALIKE_AI_ROLE', 'Nova-Testers')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


def has_ai_access(member) -> bool:
    if not hasattr(member, 'roles'):
        return False

    role_names = [role.name.lower() for role in member.roles]
    return AI_TESTER_ROLE.lower() in role_names


async def poll_api_messages():
    await bot.wait_until_ready()

    while not bot.is_closed():
        try:
            async with httpx.AsyncClient(timeout=15) as client:
                response = await client.get(
                    f'{API_BASE_URL}/bot/pending-messages',
                    headers={'X-API-Token': API_TOKEN}
                )

                data = response.json()

                for item in data.get('messages', []):
                    channel_id = item.get('channel_id') or DEFAULT_CHANNEL_ID

                    if not channel_id:
                        continue

                    channel = bot.get_channel(int(channel_id))

                    if channel:
                        await channel.send(item.get('message', '👋'))
                        logging.info(f'[NovaLike] Sent queued message to #{channel.name}')

        except Exception as e:
            logging.error(f'[NovaLike] Polling error: {e}')

        await asyncio.sleep(5)


@bot.event
async def on_ready():
    logging.info(f'[NovaLike] Connected as {bot.user}')
    logging.info(f'[NovaLike] AI tester role: {AI_TESTER_ROLE}')

    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name=STATUS
    )

    await bot.change_presence(activity=activity)
    bot.loop.create_task(poll_api_messages())


@bot.event
async def on_member_join(member):
    logging.info(f'[NovaLike] New member joined: {member.name}')

    try:
        if member.guild.system_channel:
            await member.guild.system_channel.send(
                f'👋 Bienvenue {member.mention} sur **{member.guild.name}** !'
            )
    except Exception as e:
        logging.error(f'[NovaLike] Welcome message failed: {e}')


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user and message.author.id == bot.user.id:
        return

    try:
        member_roles = []

        if hasattr(message.author, 'roles'):
            member_roles = [
                role.name
                for role in message.author.roles
                if role.name != '@everyone'
            ]

        logging.info(
            f'[NovaLike] Message from {message.author} '
            f'in #{message.channel}: {message.content[:120]}'
        )

        mentioned = bot.user in message.mentions if bot.user else False

        if mentioned and not has_ai_access(message.author):
            await message.channel.send(
                f'🔒 L’accès IA avancé de NovaLike est réservé au rôle **{AI_TESTER_ROLE}** pour éviter les abus et le spam API.'
            )
            return

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(
                f'{API_BASE_URL}/discord/message',
                json={
                    'author': str(message.author),
                    'content': message.content,
                    'channel': str(message.channel),
                    'channel_id': message.channel.id,
                    'guild': str(message.guild.name) if message.guild else None,
                    'roles': member_roles,
                    'mentioned': mentioned
                }
            )

            data = response.json()

            if data.get('should_reply'):
                reply = data.get('reply', '').strip()

                if reply:
                    await message.channel.send(reply)
                    logging.info(f'[NovaLike] Replied in #{message.channel}')

    except Exception as e:
        logging.error(f'[NovaLike] API error: {e}')

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'🏓 Pong ! `{latency}ms`')


@bot.command()
async def nova(ctx):
    await ctx.send('👋 Salut, je suis NovaLike, l’assistante communautaire WanaLike.')


@bot.command()
async def novadebug(ctx):
    if not has_ai_access(ctx.author):
        await ctx.send('⛔ Commande réservée aux testeurs NovaLike.')
        return

    await ctx.send(
        f'🧠 NovaLike Debug\n'
        f'• API: {API_BASE_URL}\n'
        f'• Role IA: {AI_TESTER_ROLE}\n'
        f'• Latence: {round(bot.latency * 1000)}ms'
    )


bot.run(TOKEN)

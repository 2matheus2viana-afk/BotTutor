import os
import discord
from dotenv import load_dotenv
from services.dify import perguntar_dify

# Carrega as variáveis do .env
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Configuração das permissões
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("=" * 40)
    print(f"✅ Bot conectado como {client.user}")
    print("=" * 40)


@client.event
async def on_message(message):
    # Ignora mensagens do próprio bot
    if message.author == client.user:
        return

    # Mostra que o bot está "digitando"
    async with message.channel.typing():
        resposta = perguntar_dify(
            pergunta=message.content,
            usuario=message.author.id
        )

    await message.channel.send(resposta)


client.run(TOKEN)
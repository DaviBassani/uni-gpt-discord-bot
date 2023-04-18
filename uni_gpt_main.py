# Bot para discord e futura inteligência artificial. Meu bot mais completo e avançado.

import discord
from discord.ext import commands
import asyncio
import uni_token
from time import sleep
from datetime import datetime
import openai
import os

class Author:
    def __init__(self) -> None:
        pass

actual_time = datetime.now()
client = discord.Client(intents=discord.Intents.all())
TOKEN = uni_token.UNITOKEN()
msg_id = None
msg_user = None
versao = ('BETA 1.0')
API = uni_token.OPENAITOKEN()
openai.api_key = API
openai.Model.list()
bot = commands.Bot(command_prefix='!uni', intents=discord.Intents.all())
prefix = '!uni'

def generate_response(message):
    prompt = message
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=500,
      top_p=1,
      stop=None,
      temperature=0.7,
    )
    return response.choices[0].text

@client.event
async def on_ready():
    print('=-' * 20)
    print('BOT ONLINE - TEXT-DAVINCI READY')
    print(client.user.name)
    print(client.user.id)
    print('CRÉDITOS: OPENAI')
    print('======DB======')
    print('=-' * 20)

@client.event
async def on_message(message):
    if not (message.author.bot):
        if message.content.startswith(prefix):
            if message.content.lower().startswith('uni_gpt'):
                await message.channel.send('UNI-GPT é um bot sem associação com a Uniasselvi e nem com a Openai, criado por alunos. O mesmo está integrado com o sistema text-davinci-003')

    # Lista de comandos
            if not (message.author.bot):
                if message.content.lower().startswith('lista de comandos'):
                    await message.channel.send('Atualmente, a única coisa que você pode fazer, é conversar com a engine text-davinci-003')

        # Atualizações e Versão
            if not (message.author.bot):
                if message.content.lower().startswith('versão'):
                    await message.channel.send('**Versão**: ``{}``'.format(versao))
                if message.content.lower().startswith('atualizações'):
                    await message.channel.send('''Aqui está a lista de todas as novas funcionalidades:\n**Versão:** {}
        **Novas funcionalidades:**

        Versão: ``{}``
        Foi adicionado integração com o ``text-davinci-003``. Para saber mais, vá para https://www.openai.com

        '''.format(versao))
                    
            if not (message.author.bot):
                if message.author == bot.user:
                    return None
                else:
            # Envie a mensagem para a API de texto da OpenAI e obtenha a resposta
                    response = generate_response(message.content)

            # Envie a resposta de volta ao canal do Discord
                    await message.channel.send('```\n' + response + '\n```')
                


client.run(TOKEN)
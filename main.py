# Bot para discord baseado em IA.

import discord
from discord.ext import commands
import asyncio
import uni_token
from time import sleep
from datetime import datetime
import openai


actual_time = datetime.now()
TOKEN = uni_token.UNITOKEN()
msg_id = None
msg_user = None
versao = ('BETA 1.1')
API = uni_token.OPENAITOKEN()
openai.api_key = API
openai.Model.list()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!uni', intents=intents)
intents.members = True
prefix = '!uni'
model_id = 'gpt-3.5-turbo'


def generate_response(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return response

conversation = []

@bot.event
async def on_ready():
    print('=-' * 20)
    print('BOT ONLINE - TEXT-DAVINCI READY')
    print(bot.user.name)
    print(bot.user.id)
    print('CRÉDITOS: OPENAI')
    print('======DB======')
    print('=-' * 20)

@bot.event
async def on_message(message):
    if not message.author.bot:

        # Sobre o bot
        if message.content.startswith(f'{prefix} sobre'):
            await message.channel.send('UNI-GPT é um bot sem associação com a Uniasselvi e nem com a Openai, criado por alunos. O mesmo está integrado com o sistema text-davinci-003')

        # Atualizações do bot
        elif message.content.startswith(f'{prefix} atualizacoes'):
            await message.channel.send(f'''Aqui está a lista de todas as novas funcionalidades:
            **Versão:** {versao}
            **Novas funcionalidades:**
            Versão: ``{versao}``
            Foi removida a integração com o ``text-davinci-003`` e adicionada a integração com o ``gpt-3.5-turbo``, a IA da OpenAI. Para saber mais, vá para https://www.openai.com
            ''')

        # Lista de comandos do bot
        elif message.content.startswith(f'{prefix} lista_de_comandos'):
            await message.channel.send('**Lista de comandos:**\n```\nlista_de_comandos_uni\natualizacoes_uni\nsobre_uni\n!uniresp + (diga aqui qualquer coisa que queira pedir à IA, e ela lhe responderá)```')

        # Resposta do bot para o usuário (OpenAI)
        elif message.content.startswith(prefix + 'resp '):
            # Adicione a mensagem do usuário à conversa
            user_message = {'role': 'user', 'content': message.content[len(prefix + 'resp '):].strip()}
            conversation.append(user_message)

            # Gere a resposta da IA
            response = generate_response(conversation)

            # Adicione a resposta da IA à conversa
            ai_message = response['choices'][0]['message']
            conversation.append({'role': ai_message['role'], 'content': ai_message['content']})

            # Envie a resposta de volta ao canal do Discord
            await message.channel.send('``UNI-GPT``' + ": " + ai_message['content'])


    await bot.process_commands(message)


bot.run(TOKEN) 
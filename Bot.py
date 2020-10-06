#Lib
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Nomeia o Bot
bot = ChatBot('Dojo_Whats')

# Treina
conv = ['oi', 'olá']
treino = ChatterBotCorpusTrainer(bot)
treino.train('chatterbot.corpus.portuguese.conversations')

# Responde
while True:
    resposta = bot.get_response(input(str()))
    print('Chat',resposta)
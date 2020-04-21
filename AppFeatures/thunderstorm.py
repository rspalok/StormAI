from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

thunderstorm_bot = ChatBot('Chatterbot',storage_adapter = "chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(thunderstorm_bot)
trainer.train("chatterbot.corpus.english")

def thunderstorm(query):
    return str(thunderstorm_bot.get_response(query))
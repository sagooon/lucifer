from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("Lucifer")

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

while True:
    user_inp = input("ME:")

    response = bot.get_response(user_inp)
    print("Lucifer: " + str(response))

# Coded with ❤️ by stdsorcerer: Github

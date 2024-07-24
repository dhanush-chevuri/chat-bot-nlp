import collections.abc
collections.Hashable = collections.abc.Hashable

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
CB = ChatBot('ChatBot')

# Training with Personal Ques & Ans
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "You're welcome.",
    "Who developed you?",
    "I am developed by Dhanush chevuri."
]

trainer = ListTrainer(CB)
trainer.train(conversation)

# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train('chatterbot.corpus.english')

# Test the chatbot
response = CB.get_response("Hello")
print(response)

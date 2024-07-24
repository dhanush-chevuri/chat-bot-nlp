from flask import Flask, render_template, request, redirect, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import collections.abc

collections.Hashable = collections.abc.Hashable

# Initialize the ChatBot
CB = ChatBot('ChatBot')
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train('chatterbot.corpus.english')

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('home'))

@app.route("/chatbot")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(CB.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)

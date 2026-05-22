import json
import random
from datetime import date
from flask import Flask, render_template, jsonify

app = Flask(__name__)

with open('sentences.json', encoding='utf-8') as f:
    SENTENCES = json.load(f)

def sentence_of_the_day():
    index = date.today().toordinal() % len(SENTENCES)
    return SENTENCES[index]

@app.route('/')
def index():
    return render_template('index.html', sentence=sentence_of_the_day())

@app.route('/random')
def random_sentence():
    return jsonify(random.choice(SENTENCES))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

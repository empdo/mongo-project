import mongo_db
import json
from flask import Flask, Response
from flask_cors import CORS
import requests

from mongo_db import LanguageType
app = Flask(__name__)
CORS(app)


@app.route('/')
def home_page():
    return 'beutyful landingpage'


@app.route('/snippets/')
@app.route('/snippets/<lang>')
def get_snippets(lang: str = None):
    snippets = mongo_db.list_snippets(lang)
    return Response(json.dumps(snippets), mimetype='application/json')


@app.route('/langs')
def get_langs():
    return Response(json.dumps(mongo_db.list_languages()), mimetype='application/json')

@app.route('/leaderboard')
def get_leaderboard():
    return Response(json.dumps(mongo_db.list_leaderboard()), mimetype='application/json')

@app.route('/token/<code>')
def get_token(code: str = None):
    if not code:
        return Response("Missing code", 401)
    url = "https://github.com/login/oauth/access_token"
    obj = {"client_id": "9b3060d8b4ddf1f2a7b8", "client_secret": "b150de451bff4e21764f50181037f57b2f92eb2e", "code": code}
    headers = {'Accept': 'application/json'}
    x = requests.post(url, data = obj, headers=headers)
    return x.text


if __name__ == "__main__":
    app.run(host = "127.0.0.1")

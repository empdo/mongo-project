import mongo_db
import json
from flask import Flask, Response
from flask_cors import CORS

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

if __name__ == "__main__":
    app.run()

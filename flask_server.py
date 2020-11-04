import mongo_db
import json
from flask import Flask, Response

from mongo_db import LanguageType
app = Flask(__name__)

@app.route('/snippets/<lang>')
def get_snippets(lang:str):
    if (lang == "ALL"):
        gen = (x for x in (mongo_db.list_snippets(None, True)))
        lang_list = list(gen)
        return Response(json.dumps(lang_list), mimetype='application/json')
    else:
        return Response(json.dumps(mongo_db.list_snippets(LanguageType(lang),False)), mimetype='application/json')
    #retrurna snippets för ett språk, alt returna alla snippets

@app.route('/langs')
def get_langs():
    return Response(json.dumps(mongo_db.list_languages()), mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
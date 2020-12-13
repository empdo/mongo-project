import enum
from typing import Union
from enum import Enum
from pprint import pp
import pymongo
import pprint

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

db = client['snippets-db']
l_db = client['leaderboard-db']

collection = db.snippets
l_collection = l_db.leaderboard


class LanguageType(Enum):
    PYTHON = 'python'
    JAVASCRIPT = 'javascript'
    JAVA = 'java'
    HTML = 'html'
    CSS = 'css'
    TYPESCRIPT = 'typescript'
    C = 'c'
    CSHARP = 'c#'
    CPP = 'c++'


def push_snippet(snippet: str, language: LanguageType):
    if snippet == '':
        return
    
    content = {
        "snippet": snippet,
        "language": language.value
    }

    collection.insert_one(content)


def list_snippets(language: Union[LanguageType, None, str]):
    if type(language) == str:
        language = LanguageType(language)

    cursor = collection.find(
        {"language": language.value} \
            if language else {}
    )

    return [
        {"lang": item["language"], "snippet": item["snippet"]} \
            for item in cursor
    ]


def list_languages():
    return collection.distinct('language')

def push_user_score(user_id: str, time):
    user = l_collection(find_one({'github-id': user_id}))
    if user:
        l_collection.remove(user)
    
    content = {
            "github-id": user_id,
                "cpm": time
            }
    l_collection.insert_one(content)
    l_collection.find().sort("time", pymongo.DESCENDING)

def list_leaderboard():
    cursor = l_collection.find()

    return [
            {"github-id": item["github-id"], "cpm" : item["cpm"]} \
            for item in cursor
    ]

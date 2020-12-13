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
l_collection = db.leaderboard


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

def push_user_score(profilepic_url: str, username: str, time):
    user = l_collection(find_one({'username': username}))
    if user:
        l_collection.remove(user)
    
    content = {
                "profile-pic": profilepic_url,
                "user-name": username,
                "cpm": time
            }
    l_collection.insert_one(content)
    l_collection.find().sort("time", pymongo.DESCENDING)

def list_leaderboard():
    return l_collection

import enum
from enum import Enum
from pprint import pp
import pymongo
import pprint

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

db = client['snippets-database']

collection = db.snippets

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
    #hämta grejer från lowlight lista


def push_snippet(snippet:str, language:LanguageType):
    content = {
        "snippet": snippet,
        "language": language.value}

    collection.insert_one(content)
    

def list_snippets(language:LanguageType, list_all:bool):
    if (list_all):
        cursor = collection.find()
        return [({"lang": item["language"], "snippet": item["snippet"]} for item in cursor)]
    else:
        return((collection.find({'language': language.value}).distinct('snippet')))

def list_languages():
    return(collection.distinct('language'))
    
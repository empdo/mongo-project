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


def pushSnippet(snippet:str, language:LanguageType):
    content = {
        "snippet": snippet,
        "language": language.value}

    collection.insert_one(content)
    

def list_snippets(language:LanguageType):
    return(list(collection.find({'language': language.value})))

pushSnippet("def alve2()", LanguageType.PYTHON)
pprint.pprint(list_snippets(LanguageType.JAVASCRIPT))
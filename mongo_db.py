import enum
from typing import Union
from enum import Enum
from pprint import pp
import pymongo
import pprint

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

db = client['test']

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


def push_snippet(snippet: str, language: LanguageType):
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

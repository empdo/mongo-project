import argparse
from argparse import ArgumentParser
import mongo_db
from mongo_db import push_snippet
from termcolor import colored

content = []


def handel_snippet(path: str, lang: mongo_db.LanguageType):
    try:
        with open(path, 'r') as f:
            for line in f:
                mongo_db.push_snippet(line.strip(), lang) 

            #spara det man senast pushade up för att kunna ta bort det

            print(colored("snippets pushed succesfully", 'green'))
    except FileNotFoundError:
        print(colored(f'not a valid path: "{path}"', 'red'))
    except:
        print(colored("Unexpected error", 'red'))


def print_snippets(lang: str):
    print(mongo_db.list_snippets(lang))


parser = argparse.ArgumentParser(prog='mongo_manager',
                                 usage="Will allow you to manage you mongodatabase",
                                 description="Allows you to manage your mongo database",
                                 add_help=True
                                 )
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--push', type=str,
                   metavar='', help='add path of file to be pushed after "-p"')
group.add_argument('-lss', '--list_snippets', type=str,
                   metavar='', help='list snippets')
parser.add_argument('-lang', type=mongo_db.LanguageType,
                    metavar='', help='language for earlier command')

args = parser.parse_args()


if __name__ == "__main__":
    if args.push:
        handel_snippet(args.push, args.lang)
    elif args.list_snippets:
        print_snippets(args.lang)

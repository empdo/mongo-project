import argparse
from argparse import ArgumentParser
import mongo_db
from mongo_db import push_snippet

content = []


def handel_snippet(path: str, lang: str):
    try:    
        with open(path, 'r') as f:
            i = 0
            for line in f:
                content.append(line.strip())
        mongo_db.push_snippet(path, lang)
    except FileNotFoundError as e:
        print(e)
    except:
        print("Unexpected error")



def print_snippets(lang: str):
    print(lang)


parser = argparse.ArgumentParser(prog='mongo_manager',
                                 usage="Will allow you to manage you mongodatabase",
                                 description="Allows you to manage your mongo database",
                                 add_help=True
                                 )
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--push', type=str,
                   metavar='', help='add path of file to be pushed as snippets')
group.add_argument('-lss', '--list_snippets', type=str,
                   metavar='', help='list snippets')
parser.add_argument('-lang', type=str,
                    metavar='', help='language for earlier command')

args = parser.parse_args()


if __name__ == "__main__":
    for x in mongo_db.LanguageType:
        if x.value in args.lang:
            if args.push:
                handel_snippet(args.push, args.lang)
            elif args.list_snippets:
                print_snippets(args.lang)
        else:
            print("Not a valid language, please try again")
            #return to help page
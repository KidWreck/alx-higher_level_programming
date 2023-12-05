#!/usr/bin/python3
'''6. Create object from a JSON file.'''


import json


def load_from_json_file(filename):
    '''Creates an object from a JSON file.'''
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)

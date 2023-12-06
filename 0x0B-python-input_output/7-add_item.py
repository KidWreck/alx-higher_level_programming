#!/usr/bin/python3
'''7. Load, add, save.'''


import sys
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])

try:
    old = load_json('add_item.json')
except Exception:
    old = []

old.extend(args)
save_json(old, 'add_item.json')

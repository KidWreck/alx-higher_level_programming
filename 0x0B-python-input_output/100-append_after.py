#!/usr/bin/python3
'''13. Search and update.'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file
    after each line containing a specific string.'''
    with open(filename, "r", encoding="utf-8") as f:
        ll = []
        while True:
            line = f.readline()
            if line == "":
                break
            ll.append(line)
            if search_string in line:
                ll.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(ll)

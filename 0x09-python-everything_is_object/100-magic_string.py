#!/usr/bin/python3
def magic_string():
    magic_string.h = getattr(magic_string, 'h', 0) + 1
    return ", ".join(["Best School" for i in range(magic_string.h)])

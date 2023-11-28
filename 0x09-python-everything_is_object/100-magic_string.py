#!/usr/bin/python3
def magic_string():
    magic_string.h = getattr(magic_string, 'h', 0) + 1
    return ("Best School, " * (magic_string.h - 1) + "Best School")

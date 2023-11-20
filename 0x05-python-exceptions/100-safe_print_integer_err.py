#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    p = True
    try:
        print("{:d}".format(value)))
    except Exception as err:
        print("Exception:", e, file = sys.stderr)
        p = False
    return p

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size == 0:
        print ("0 arguments.")
    elif size == 1:
        print ("1 argumnets.")
    else:
        print("{} arguments:".format(size))
    for i in range(size):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

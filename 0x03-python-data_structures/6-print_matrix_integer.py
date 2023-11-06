#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for m in matrix:
        if len(m) == 0:
            print()
        for n in range(len(m)):
            print("{:d}".format(m[i]), end = "\n" if i is len(m) - 1 else " ")

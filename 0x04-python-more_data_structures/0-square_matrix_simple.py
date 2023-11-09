#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = []
    for i in matrix:
        sq.append([x ** 2 for x in i])
    return sq

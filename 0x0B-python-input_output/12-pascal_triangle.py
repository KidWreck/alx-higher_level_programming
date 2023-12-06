#!/usr/bin/python3
'''12. Pascal's Triangle.'''


def pascal_triangle(n):
    '''Returns a list of lists of integers representing
    the Pascal's triangle of n.'''
    if n <= 0:
        return []
    tri = [[1]]
    while len(tri) != n:
        m = tri[-1]
        tmp = [1]
        for i in range(len(m) - 1):
            tmp.append(m[i] + m[i+1])
        tmp.append(1)
        tri.append(tmp)
    return tri

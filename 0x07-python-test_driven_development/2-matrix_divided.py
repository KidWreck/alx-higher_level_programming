#!/usr/bin/python3
'''Divide a matrix.'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of matrix by div.

    Args:
        matrix: List of lists (matrix) of int or float.
        div: number to divide matrix by.

    Returns:
        List of lists (matrix) representing divided matrix.

    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    '''
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for x in matrix:
        if not isinstance(x, list) or len(x) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(x) != len(matrix[0]):
            raise TypeError("Each x of the matrix must have the same size")
        for i in x:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
    return [[round(i / div, 2) for i in x] for x in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

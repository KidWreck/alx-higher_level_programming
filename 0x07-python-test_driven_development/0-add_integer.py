#!/usr/bin/python3
'''Integers addition.'''


def add_integer(a, b=98):
    '''
    Adds two int.

    Args:
        a: int.
        b: int = 98.

    Raises:
        TypeError: if a or b are not int or float.

    Returns:
        The sum of a + b.
    '''

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

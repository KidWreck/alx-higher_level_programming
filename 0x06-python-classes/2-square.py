#!/usr/bin/python3
'''Third quiz.'''

class Square:
    '''This my square.'''

    def __init__(self, size=0):
        '''Initaloize.

        Args:
            size: length of a side.

        Raises:
            TypeError: size not int
            VlueError: size < 0
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

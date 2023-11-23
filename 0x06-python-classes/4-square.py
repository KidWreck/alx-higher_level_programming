#!/usr/bin/python3

'''This is the 5th quiz module.'''


class Square:
    '''This my square.'''

    def __init__(self, size=0):
        '''Initaloize.

        Args:
            size: length of a side.
        '''
        self.size = size

    @property
    def size(self):
        '''Property for the lenghth of squaer's side.

        Raises:
            TypeError: size not int
            VlueError: size < 0
        '''
        return self.__size

    @size.setter
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        '''Area of square

        Return:
            Area.
        '''
        return self.__size ** 2

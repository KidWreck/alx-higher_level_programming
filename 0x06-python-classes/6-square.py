#!/usr/bin/python3
'''6th quiz.'''

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

    @property
    def position(self):
        '''Get/set the coordinates'''
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) fot n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        '''Area of square

        Return:
            Area.
        '''
        return self.__size ** 2

    def my_print(self):
        '''Print the square.'''
        if self.__size == 0:
            print()
            return
        for x in range(0, self.__position[1]):
            print()
        for x in range(0, self.__size):
            for z in range(0, self.__position[0]):
                print(" ", end="")
            for y in range(0, self.__size):
                print("#", end="")
            print()

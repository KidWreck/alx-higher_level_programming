#!/usr/bin/python3
'''10. Square #1.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Subclass for square.'''

    def __init__(self, size):
        ''' Init.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Area of square.'''
        return self.__size ** 2
    
    def __str__(self):
        '''String representation.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

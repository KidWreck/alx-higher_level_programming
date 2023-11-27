#!/usr/bin/python3
'''1. Real definition of a rectangle'''


class Rectangle:
    '''Class Rectangle that defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''init the rectangle'''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''getter for private attribute'''
        return self.__width
    
    @width.setter
    def width(self, val):
        '''setter for private attribute'''
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def highet(self):
        '''getter for private attribute'''
        return self.__highet
    
    @highet.setter
    def highet(self, val):
        '''setter for private attribute'''
        if type(val) is not int:
            raise TypeError("highet must be an integer")
        if val < 0:
            raise ValueError("highet must be >= 0")
        self.__highet = val

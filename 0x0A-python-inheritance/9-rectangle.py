#!/usr/bin/python3
'''9. Full rectangle.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Subclass for rectangle.'''

    def __init__(self, width, height):
        '''Init.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Area of rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''String representation.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

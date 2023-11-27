#!/usr/bin/python3
"""1. Real definition of a rectangle."""


class Rectangle:
    """Class Rectangle that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Init the rectangle."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for private attribute."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter for private attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private attribute."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter for private attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

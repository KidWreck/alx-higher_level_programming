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
    def highet(self):
        """Getter for private attribute."""
        return self.__highet
    
    @highet.setter
    def highet(self, value):
        """Setter for private attribute."""
        if type(value) is not int:
            raise TypeError("highet must be an integer")
        if value < 0:
            raise ValueError("highet must be >= 0")
        self.__highet = value

   def area(self):
        """Calculate the area."""
        return self.__width * self.__highet

    def perimeter(self):
        """Calculate the perimeter."""
        if self.__width == 0 or self.__highet == 0:
             return 0
        return ((self.__width + self.__highet) * 2)

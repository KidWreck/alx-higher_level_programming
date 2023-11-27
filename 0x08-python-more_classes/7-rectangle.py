#!/usr/bin/python3
"""7. Change representation."""


class Rectangle:
    """Class Rectangle that defines a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init the rectangle."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculate the area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return a string of '#' rectangle."""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") * self.height)

    def __repr__(self):
        """Return a represintaition of '#' rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete every rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

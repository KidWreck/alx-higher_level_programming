#!/usr/bin/python3
'''Encoding assembly.'''

import math

class MagicClass:
    '''My circle'''

    def __init__(self, radius=0):
        ''' Initialize.
        Arg:
            radius (float or int): The radius.'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''return the area of the circle'''
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        '''return the circumference of the circle'''
        return (self.__radius * 2 * math.pi)

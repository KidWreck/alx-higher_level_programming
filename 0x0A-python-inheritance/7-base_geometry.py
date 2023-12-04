#!/usr/bin/python3
'''7. Integer validator.'''


class BaseGeometry:
    '''BaseGeometry class.'''

    def area(self):
        '''Area error.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

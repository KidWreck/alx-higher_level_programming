#!/usr/bin/python3
'''9. Student to JSON.'''


class Student:
    '''A Student.'''

    def __init__(self, first_name, last_name, age):
        '''Init.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns a dictionary represintation.'''
        return self.__dict__

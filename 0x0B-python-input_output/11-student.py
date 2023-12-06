#!/usr/bin/python3
'''11. Student to disk and reload.'''


class Student:
    '''A Student.'''

    def __init__(self, first_name, last_name, age):
        '''Init.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns a dictionary representation.'''
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        '''Replaces all attributes with JSON.'''
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value

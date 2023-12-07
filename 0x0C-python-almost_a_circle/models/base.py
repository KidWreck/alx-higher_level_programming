#!/usr/bin/python3
'''Module for Base class.'''
import json
import csv


class Base:
    '''A Base class.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Init.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#!/usr/bin/python3
'''12. My integer'''


class MyInt(int):
    '''Rebel version of an integer'''

    def __new__(cls, *args, **arg):
        '''create a new instance of the class'''
        return super(MyInt, cls).__new__(cls, *args, **arg)

    def __eq__(self, i):
        '''!= is now =='''
        return int(self) != i

    def __ne__(self, i):
        '''== is now !='''
        return int(self) == i

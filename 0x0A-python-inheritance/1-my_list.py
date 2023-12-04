#!/usr/bin/python3
'''1. My list.'''


class MyList(list):
    '''MyList class.'''

    def print_sorted(self):
        '''Prints the list, but sorted.'''
        print(sorted(self))

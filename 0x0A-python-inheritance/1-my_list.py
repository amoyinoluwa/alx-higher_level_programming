#!/usr/bin/python3
"""Custom list class"""


class MyList(list):
    """Class that inherits the list class"""
    def __init__(self):
        """Initializes the list class"""
        list.__init__(self)
    def print_sorted(self):
        """Prints all elements in the list in ascending order"""
        res = self[:]
        return sorted(res)

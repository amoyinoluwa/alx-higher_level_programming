#!/usr/bin/python3
"""A square class"""


class Square:
    """A square class"""
    def __init__(self, size=0):
        """Square class Initialization"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

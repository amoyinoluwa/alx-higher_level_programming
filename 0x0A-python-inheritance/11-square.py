#!/usr/bin/python3
"""A square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size):
        """Initializer"""
        self.__size = size
        self.integer_validator("size", self.__size)
    def area(self):
        """Calculates area"""
        return self.__size**2
    def __str__(self):
        """Returns string repr"""
        return "[{}] {}/{}".format(self.__class__.__name__, self.__size, self.__size)

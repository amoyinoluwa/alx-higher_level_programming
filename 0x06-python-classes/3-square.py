#!/usr/bin/python3
"""Definition of a square class"""
class Square:
    """A square class"""
    def __init__(self, size=0):
        """Initialization of Square class"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Method to return area of square"""
        return (self.__size**2)


#!/usr/bin/python3
"""class that defines a rectangle"""
class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization of values"""
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """Returns the width of rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """A setter for the width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """Returns the height of a rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """Sets the height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

#!/usr/bin/python3
"""Class that defines a rectangle"""
class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """Gets the width of rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """Sets the height of a rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    def area(self):
        """Calculates the area of rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        """Calculates the perimeter of rectangle"""
        res = 2 * (self.__width + self.__height)
        return res

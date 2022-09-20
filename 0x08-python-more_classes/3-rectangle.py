#!/usr/bin/python3
"""A rectangle class"""

class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes values of rectangle"""
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
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        res = 2 * (self.__width + self.__height)
        return res

    def __str__(self):
        """Returns the string representation"""
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res
        for i in range(self.__height):
            for i in range(self.__width):
                res += "#"
            res += '\n'
        return res[:-1]

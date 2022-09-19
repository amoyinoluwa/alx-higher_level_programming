#!/usr/bin/python3
"""A rectangle class"""
class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
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
        """Sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__width
    def perimeter(self):
        """Returns the perimeter of rectangle"""
        res = 2 * (self.__height + self.__width)
        return res
    def __str__(self):
        """Returns the string representation"""
        res = ""
        for i in range(self.__height):
            for i in range(self.__width):
                res += "#"
            res += '\n'
        return res[:-1]
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        return print("Bye rectangle...")

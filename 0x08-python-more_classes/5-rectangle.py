#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes value of rectangle"""
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
            self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        res = 2 * (self.__height + self.__width)
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

    def __repr__(self):
        """Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deletes a rectangle instance"""
        print("Bye rectangle...")

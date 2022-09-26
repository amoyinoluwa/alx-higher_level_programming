#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Class initializer"""
        BaseGeometry.__init__(self)
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
    def area(self):
        """Calculates the area of rectangle"""
        return self.__width * self.__height
    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)

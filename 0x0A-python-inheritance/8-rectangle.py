#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

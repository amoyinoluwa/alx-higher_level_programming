#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def __init__(self):
        """Initializer"""
        pass
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validates inputs"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))

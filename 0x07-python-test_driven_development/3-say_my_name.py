#!/usr/bin/python3
"""Prints "My name is" followed by input string"""


def say_my_name(first_name, last_name=""):
    """prints "My name is"
    Args:
        first_name (str): first name
        last_name (str): last name
    Raises:
        TypeError: if either first_name or last_name are not strings
    """
    if type(first_name) is str:
        if type(last_name) is str:
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")

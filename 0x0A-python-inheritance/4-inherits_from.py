#!/usr/bin/python3
"""checks if object inherits from a class"""

def inherits_from(obj, a_class):
    """checks if object inherits from a class"""
    return False if type(obj) is a_class else isinstance(obj, a_class)

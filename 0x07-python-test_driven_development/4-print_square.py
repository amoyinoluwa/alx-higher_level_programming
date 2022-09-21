#!/usr/bin/python3
"""prints a square"""


def print_square(size):
    """Method to print a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("#" * size)

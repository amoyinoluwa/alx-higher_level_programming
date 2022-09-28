#!/usr/bin/python3
"""Openeing a file in python"""


def read_file(filename=""):
    """reading a python file"""

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())

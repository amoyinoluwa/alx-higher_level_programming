#!/usr/bin/python3

def write_file(filename="", text=""):
    """writes to a file"""

    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count

#!/usr/bin/python3
"""Definition of a square class"""
class Square:
    """Definition of a square class"""
    def __init__(self, size=0):
        """Initializes the size of the square"""
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size of the square"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of the square"""
        return (self.__size**2)
    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()

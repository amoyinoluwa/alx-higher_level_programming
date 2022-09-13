#!/usr/bin/python3
"""Definition of a square class"""
class Square:
    """Definition of a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size of the square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @property
    def position(self):
        return self.__position

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

    @position.setter
    def position(self, value):
        """Method to set position"""
        if not (type(value).__name__ == "tuple" and len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square"""
        return (self.__size**2)

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                print(' ' * self.position[0] + '#' * self.size)

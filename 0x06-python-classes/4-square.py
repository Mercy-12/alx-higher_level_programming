#!/usr/bin/python3
class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new data"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

#!/usr/bin/python3
class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

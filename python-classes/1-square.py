#!/usr/bin/python3
"""
1-square.py
A module that defines a Square class for working with squares.
"""
class Square:
    """
    A class that defines a square based on a given size.

    Attributes:
        __size (int): The size of the square's sides.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square's sides. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

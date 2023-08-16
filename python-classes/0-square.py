#!/usr/bin/python3
"""
0-square.py
A module that defines a Square class for working with squares.
"""

class Square:
    """
    A class that defines a square based on a given size.

    Attributes:
        __size (int): The size of the square's sides.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.__size

    def get_size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    def set_size(self, size):
        """
        Sets the size of the square to the given value.

        Args:
            size (int): The new size for the square's sides.
        """
        self.__size = size

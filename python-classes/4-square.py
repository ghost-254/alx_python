#!/usr/bin/python3
"""
4-square.py
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
        self.size = size  # Using the setter to set the size attribute

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size for the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.

        If the size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
            return
        
        for _ in range(self.__size):
            print("#" * self.__size)

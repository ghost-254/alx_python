#!/usr/bin/python3
class Square:
    """
    This class defines a square by its size.

    Attributes:
        __size (int): The size of the square's sides.

    Methods:
        get_size(): Returns the size of the square.
        set_size(new_size): Sets the size of the square (non-negative).
        __str__(): Returns a string representation of the square.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
    
    def get_size(self):
        """
        Returns the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size
    
    def set_size(self, new_size):
        """
        Sets the size of the square.

        Args:
            new_size (int): The new size of the square's sides.

        Raises:
            ValueError: If the new size is negative.
        """
        if new_size >= 0:
            self.__size = new_size
        else:
            raise ValueError("Size cannot be negative")
    
    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string describing the square.
        """
        return f"Square with side length {self.__size}"

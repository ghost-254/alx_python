#!/usr/bin/python3
"""
5-base_geometry.py
A module that defines the BaseGeometry class for representing a base geometry.
"""

class BaseGeometry:
    """
    A class representing a base geometry.

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
        integer_validator(self, name, value): Validates an integer value.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value as an integer.

        Args:
            name (str): The name associated with the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# 7-rectangle.py
"""
7-rectangle.py
A module that defines the Rectangle class, inheriting from BaseGeometry (5-base_geometry.py), for representing a rectangle.
"""
class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): Private attribute representing the width of the rectangle.
        __height (int): Private attribute representing the height of the rectangle.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the provided width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validating and setting the private attributes for width and height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A formatted string describing the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

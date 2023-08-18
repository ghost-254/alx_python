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

# 6-rectangle.py
"""
6-rectangle.py
A module that defines the Rectangle class, inheriting from BaseGeometry (5-base_geometry.py), for representing a rectangle.
"""
class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """ 
        Initializes a Rectangle instance with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = None
        self.__height = None
        """
        Initializes private variables for width and height with None
        """
        self.integer_validator("width", width)
        """
        Validates and sets the "width" attribute using the integer_validator method
        """
        self.integer_validator("height", height)
        """
        Validate and set the "height" attribute using the integer_validator method
        """
        self.__width = width
        """
        Assigns the validated width to the private attribute __width
        """
        self.__height = height
        """
        Assigns the validated height to the private attribute __height
        """

#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size
    
    def __str__(self):
        return f"Square with side length {self.__size}"

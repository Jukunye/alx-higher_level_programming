#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """class represents a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object with optional width and height.

        Args:
            width (int, optional): The width of the rectangle.
            height (int, optional): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value to be set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value to be set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

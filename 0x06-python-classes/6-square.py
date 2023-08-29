#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
            size (init): size of a side of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of the object.

        Returns:
            int: The size of the object.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the object.

        Args:
            Value (int): The new size value to be set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    @property
    def position(self):
        """
        Get the position of the object.

        Returns:
            tuple: The position of the object.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

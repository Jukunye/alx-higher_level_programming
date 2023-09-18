#!/usr/bin/python3
"""
This module defines a 'Square' class which is a subclass of 'Rectangle'
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the top-left corner.
        y (int): The y-coordinate of the top-left corner.
        id (int): The unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square Object"""
        super().__init__(size, size, x, y, id=id)

    @property
    def size(self):
        """Get the  size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns Square representation
        [Square] (<id>) <x>/<y> - <size>
        """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            num = len(args)
            if num >= 1:
                self.id = args[0]
            if num >= 2:
                self.size = args[1]
            if num >= 3:
                self.x = args[2]
            if num >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

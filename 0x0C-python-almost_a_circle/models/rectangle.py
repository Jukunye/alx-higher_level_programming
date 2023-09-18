#!/usr/bin/python3
"""
This module defines rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle

    Args:
        width (int): The width of the rectanle
        height (int): The height of the rectangle
        x (int optional): The x-cordinate of the rectangle position
        y (int optional): The y-cordinate of the rectangle position
        id (int): The identifier for the rectangle

    Note:
        This class inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __validate_int(self, value, name, positive=True):
        """
        Validates that 'value' is an integer and, optionally, positive.
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if positive and value <= 0:
            raise ValueError(f'{name} must be > 0')
        elif not positive and value < 0:
            raise ValueError(f'{name} must be >= 0')

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Retangle"""
        self.__validate_int(value, 'width', positive=True)
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Retangle"""
        self.__validate_int(value, 'height', positive=True)
        self.__height = value

    @property
    def x(self):
        """Returns the x-cordinate of the Rectangle's position"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-cordinate of the Rectangle's position"""
        self.__validate_int(value, 'x', positive=False)
        self.__x = value

    @property
    def y(self):
        """Get the y-cordinate of the rectangle's position"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y-cordinate of the rectangle's position"""
        self.__validate_int(value, 'y', positive=False)
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle"""
        return self.height * self.width

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Returns Rectangle representation
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f'[Rectangle] ({self.id}) {self.x}/{self.y}' \
            f' - {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            num = len(args)
            if num >= 1:
                self.id = args[0]
            if num >= 2:
                self.width = args[1]
            if num >= 3:
                self.height = args[2]
            if num >= 4:
                self.x = args[3]
            if num >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

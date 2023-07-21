#!/usr/bin/python3

"""Defines a rectangle model class."""
import json
import csv
import turtle
from models.base import Base


class Rectangle(Base):
    """Rectangle model.

    This Represents the Class Rectangle.

    Private Class Attributes:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        x (int): The x coordinate of the new Rectangle.
        y (int): The y coordinate of the new Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value >= 0:
            self.__width = value
        else:
            raise ValueError("Width cannot be negative.")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value >= 0:
            self.__height = value
        else:
            raise ValueError("Height cannot be negative.")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

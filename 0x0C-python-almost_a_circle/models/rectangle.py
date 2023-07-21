#!/usr/bin/python3

"""Defines a rectangle model class."""
import json
import csv
import turtle
from base import Base


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

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    # Setter methods
    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

#!/usr/bin/python3
"""Defines a rectangle model class."""
from models.rectangle import Rectangle


class Square (Rectangle):
    """Rectangle square.

    This Represents the Class square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        print (id,"dans square ")
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Custom string representation for Square.

        Returns:
            str: A formatted string representing the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
    
    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
    def update(self, *args, **kwargs):
        """Update the rectangle

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) > 0:
                self.id = args[0]
                if len(args) > 1:
                    self.width = args[1]
                    self.height = args[1]
                    if len(args) > 2:
                        self.x = args[2]
                        if len(args) > 3:
                            self.y = args[3]                                   
        elif len(kwargs) > 0 :
            for key, value in kwargs.items():
                attributes = {
                    "id": lambda v: setattr(self, "id", v) if v is not None else self.__init__(self.width, self.height, self.x, self.y),
                    "size": lambda v: setattr(self, "width", v) or setattr(self, "height", v),
                    "x": lambda v: setattr(self, "x", v),
                    "y": lambda v: setattr(self, "y", v),
                }

                update_attribute_func = attributes.get(key)
                if update_attribute_func:
                    update_attribute_func(value)
            
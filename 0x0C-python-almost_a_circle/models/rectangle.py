#!/usr/bin/python3
"""
This is the Rectangle Class Inheriting from Base
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ X Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ X Setter """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ Y Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y Setter """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Area Method """
        return self.__width * self.__height

    def display(self):
        """ Draws a Rectangle Pattern """
        string1 = ('\n' * self.y)
        string2 = ((" " * self.x) + '#' * self.__width + '\n') * (
                (self.__height) - 1)
        string3 = ((" " * self.x) + '#' * self.__width)
        print(string1 + string2 + string3)

    def __str__(self):
        """ String Method """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Method to Update Class Attributes """
        if args:
            if args[0] is not None and args[0] != self.id:
                self.id = args[0]
            elif args[1] is not None and args[1] != self.width:
                self.width = args[1]
            elif args[2] is not None and args[2] != self.height:
                self.height = args[2]
            elif args[3] is not None and args[3] != self.x:
                self.x = args[3]
            elif args[4] is not None and args[4] != self.y:
                self.y = args[4]
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs['id']
                if key == 'width':
                    self.width = kwargs['width']
                if key == 'height':
                    self.height = kwargs['height']
                if key == 'x':
                    self.x = kwargs['x']
                if key == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        """ Method to Return the Dictionary Representation """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary

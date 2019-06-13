#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs['id']
                if key == 'size':
                    self.width = kwargs['size']
                if key == 'x':
                    self.x = kwargs['x']
                if key == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
            class_dict = {}
            class_dict['id'] = self.id
            class_dict['size'] = self.width
            class_dict['x'] = self.x
            class_dict['y'] = self.y
            return class_dict

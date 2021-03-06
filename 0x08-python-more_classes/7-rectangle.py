#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ("")
        custom_symbol = str(self.print_symbol)
        string = (custom_symbol * self.__width + '\n') * (
            self.__height - 1) + (custom_symbol * self.__width)
        return string

    def __repr__(self):

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print('Bye rectangle...')

        Rectangle.number_of_instances -= 1

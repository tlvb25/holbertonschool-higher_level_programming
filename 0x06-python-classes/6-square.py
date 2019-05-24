#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def size(self):
        return self.__size

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError('size must be an integer')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('size must be an integer')
        elif type(value[0]) < 0 or type(value[1]) < 0:
            raise TypeError('size must be an integer')
        self.__position = value

    @property
    def position(self):
        return self.__position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(1, self.__size + 1):
                print('#', end='')
            print()

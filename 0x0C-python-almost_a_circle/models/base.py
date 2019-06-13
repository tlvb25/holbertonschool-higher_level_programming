#!/usr/bin/python3
"""
This module will be the “Base” of all other classes in this project.
"""


import json
import os


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=[]):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list = [] if list_objs is None else [
                x.to_dictionary() for x in list_objs]
        filename = cls.__name__ + '.json'
        with open(filename, mode='w+') as a_file:
            a_file.write(cls.to_json_string(list))

    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(8, 8, 8, 8)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        with open(filename, mode='r') as a_file:
            if a_file:
                file_read = a_file.read()
            else:
                return []
        new_list = []
        file_read_list = cls.from_json_string(file_read)
        for elements in file_read_list:
            new_list.append(cls.create(**elements))
        return new_list

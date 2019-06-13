#!/usr/bin/python3
"""Unittest for base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    def test_base_exist(self):
        a = Base()
        assert a

    def test_base_autoassign_id(self):
        a = Base()
        assert a.id = 2

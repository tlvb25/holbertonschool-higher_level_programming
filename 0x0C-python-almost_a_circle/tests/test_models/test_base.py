#!/usr/bin/python3
"""Unittest for base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    
    
    def setUp(self:
        Base._Base__nb_objects = 0
    
    def test_base_autoassign_id(self):
        a = Base()
        self.assertEqual(a.id, 1)

    def test_baseid_plus_one(self):
        a = Base()
        b = Base()
        self.assertEqual(b.id, 2)

    def test_saving_id(self):
        a = Base(89)
        self.assertEqual(a.id, 89)

    def Base_to_json_str(self):
        Base.to_json_string(None)
        self.assertEqual(Base.to_json_string(None), [])

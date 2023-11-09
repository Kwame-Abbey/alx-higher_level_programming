#!/usr/bin/python3
"""Defines test cases for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class that inherits unittest"""

    def test_import(self):
        self.assertTrue(Base)

    def test_private_class_attribute(self):
        self.assertEqual(Base._Base__nb_objects, 0)
        obj = Base()
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_default_constructor(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_constructor_with_id(self):
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_uniqueness_of_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

#!/usr/bin/python3
import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseDocs(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)


class TestBase(unittest.TestCase):
    """ tests for class Base """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        Base._Base__nb_objects = 0
        cls.obj1 = Base()
        cls.obj2 = Base()
        cls.obj3 = Base(56)
        cls.obj4 = Base()
        cls.obj5 = Base("six")
        cls.obj6 = Base(7.6)
        cls.r1 = Rectangle(1, 1, 0, 0, 1)

    def test_id(self):
        """ test id attribute """
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 2)
        self.assertEqual(self.obj3.id, 56)
        self.assertEqual(self.obj4.id, 3)
        self.assertEqual(self.obj5.id, "six")
        self.assertEqual(self.obj6.id, 7.6)

    def test_to_json(self):
        """ test to_json_string method """
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        d1 = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}
        json_test = Base.to_json_string(d1)
        self.assertTrue(type(json_test) is str)
        test_dict = json.loads(json_test)
        self.assertEqual(test_dict, d1)

    def test_from_json(self):
        """ test from_json_string method """
        self.assertEqual(Base.from_json_string([]), [])
        self.assertEqual(Base.from_json_string(None), [])

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass

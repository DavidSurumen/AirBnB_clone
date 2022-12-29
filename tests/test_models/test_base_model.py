#!/usr/bin/python3
"""Test module for base_model.py"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Implements test cases for class BaseModel."""

    def test_has_attributes(self):
        """Asserts that instance attributes are created."""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(hasattr(obj, 'id'))

    def test_id_is_string(self):
        """Asserts that the attribute 'id' is converted to string."""
        obj = BaseModel()
        self.assertTrue(type(obj.id), str)

    def test_save(self):
        """Tests that 'updated_at' is not having the same
        value as 'created_at'."""
        obj = BaseModel()

        self.assertEqual(obj.created_at, obj.updated_at)
        obj.save()
        self.assertNotEqual(obj.updated_at, obj.created_at)

    def test_to_dict(self):
        """Asserts that the method to_dict() returns a dictionary from the
        __dict__ of an instance."""

        obj = BaseModel()
        dct = obj.to_dict()

        self.assertTrue(type(dct), dict)

    def test_to_dict_iso(self):
        """Asserts that the attributes 'created_at' and 'updated_at' are
        ISO formatted."""

        obj = BaseModel()
        dct = obj.to_dict()

        self.assertTrue(type(dct.get('created_at')), str)
        self.assertTrue(type(dct.get('updated_at')), str)

    def test_to_dict_has_class(self):
        """Asserts that the dictionary returned has the key '__class__'."""

        obj = BaseModel()
        dct = obj.to_dict()

        self.assertEqual(dct.get('__class__'), 'BaseModel')


if __name__ == '__main__':
    unittest.main()

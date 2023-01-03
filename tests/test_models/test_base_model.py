#!/usr/bin/python3
"""Test module for base_model.py"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import uuid
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Implements test cases for class BaseModel."""
    def setUp(self):
        """setup code to be ran for every test."""

        self.obj = BaseModel()  # for the tests that need
        self.obj.save()

    def test_has_attributes(self):
        """Asserts that instance attributes are created."""

        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))
        self.assertTrue(hasattr(self.obj, 'id'))

    def test_id_is_string(self):
        """Asserts that the attribute 'id' is converted to string."""

        self.assertTrue(type(self.obj.id), str)

    def test_save(self):
        """Tests that 'updated_at' is not having the same
        value as 'created_at'."""

        self.assertNotEqual(self.obj.updated_at, self.obj.created_at)

    def test_to_dict(self):
        """Asserts that the method to_dict() returns a dictionary."""

        dct = self.obj.to_dict()
        self.assertTrue(type(dct), dict)

    def test_to_dict_iso(self):
        """Asserts that the attributes 'created_at' and 'updated_at' are
        ISO formatted."""

        dct = self.obj.to_dict()
        self.assertTrue(type(dct.get('created_at')), str)
        self.assertTrue(type(dct.get('updated_at')), str)

    def test_to_dict_has_class(self):
        """Asserts that the dictionary returned has the key '__class__'."""

        dct = self.obj.to_dict()
        self.assertEqual(dct.get('__class__'), 'BaseModel')

    def tearDown(self):
        """tidy up after setUp method is called."""

        FileStorage._FileStorage__objects = {}    # resets the attribute

        fl = FileStorage._FileStorage__file_path    # path to the saved file
        if os.path.isfile(fl) is True:
            os.remove(fl)

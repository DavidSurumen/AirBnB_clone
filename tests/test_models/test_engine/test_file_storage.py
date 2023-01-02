#!/usr/bin/python3
"""Tests for the Storage module."""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
import os


class TestFileStorage(unittest.TestCase):
    """Implementation of tests for the FileStorage class."""
    def setUp(self):
        """setup ran for every test"""
        self.obj = FileStorage()

    def test_instances(self):
        """chequeamos instantiation."""

        self.assertIsInstance(self.obj, FileStorage)

    def test_all(self):
        """tests that all() returns a dictionary."""

        self.assertEqual(type(self.obj.all()), dict)

    def test_new(self):
        """tests the new() method."""

        BaseModel()  # calls storage.new(), creates a new object
        test_dict = FileStorage._FileStorage__objects

        self.assertTrue(bool(test_dict), '__objects dict is empty')

    def test_new_stored_objects(self):
        """tests that objects are stored properly by new()."""

        BaseModel()
        test_dict = FileStorage._FileStorage__objects

        for key in test_dict.keys():
            self.assertEqual(type(key), str, 'key should be type str')
            self.assertEqual(type(test_dict[key]), dict,
                             'must store dictionaries')

    def test_save(self):
        """asserts that __objects dict is serialized to a JSON file"""

        self.obj.save()

        file_ = os.path.join(FileStorage._FileStorage__file_path, 'file.json')
        self.assertTrue(os.path.isfile(file_), 'file does not exist')

    def test_reload(self):
        """tests the reload() method."""

        BaseModel()   # create a new test object - constructor calls new()
        self.obj.save()   # persist the new object to a file.
        self.obj.reload()   # reload the object to the dict variable __objects

        dct = FileStorage._FileStorage__objects
        self.assertTrue(bool(dct), 'reloaded dictionary must not be empty')

    def tearDown(self):
        """cleans up afters each run of a test."""

        FileStorage._FileStorage__objects = {}  # resets the variable
        fl = os.path.join(FileStorage._FileStorage__file_path, 'file.json')
        if os.path.isfile(fl):
            os.remove(fl)

#!/usr/bin/python3
"""Tests for the Storage module."""
import unittest
from models.engine.file_storage import FileStorage
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

    def test_save(self):
        """asserts that __objects dict is serialized to a JSON file"""

        self.obj.save()

        file_ = os.path.join(FileStorage._FileStorage__file_path, 'file.json')
        self.assertTrue(os.path.isfile(file_), 'file does not exist')

    def tearDown(self):
        """cleans up afters each run of a test."""

        fl = os.path.join(FileStorage._FileStorage__file_path, 'file.json')
        if os.path.isfile(fl):
            os.remove(fl)

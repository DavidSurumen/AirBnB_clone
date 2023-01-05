#!/usr/bin/python3
"""Tests for State module"""
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def setUp(self):
        """sets up the tests for the class."""
        self.obj = State()

    def test_parent(self):
        """Tests that State class inherits from BaseModel class"""

        self.assertTrue(isinstance(self.obj, State))
        self.assertTrue(isinstance(self.obj, BaseModel))

    def test_hasattr(self):
        """Tests the attributes of the State class"""

        self.assertTrue(hasattr(self.obj, 'name'))

    def test_atrr_values(self):
        """Tests the default value for attributes."""

        self.assertEqual(self.obj.name, '')

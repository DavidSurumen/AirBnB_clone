#!/usr/bin/python3
"""Test module for city.py"""
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """sets up the tests."""
        
        self.obj = City()

    def test_parent(self):
        """Tests for inheritance from BaseModel"""

        self.assertTrue(isinstance(self.obj, City))
        self.assertTrue(isinstance(self.obj, BaseModel))

    def test_hasattribs(self):
        """Tests that the class has the right public attributes"""

        self.assertTrue(hasattr(self.obj, 'state_id'))
        self.assertTrue(hasattr(self.obj, 'name'))

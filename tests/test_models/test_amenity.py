#!/usr/bin/python3
"""Test suite for amenity class"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        """sets up test cases"""

        self.obj = Amenity()

    def test_parent(self):
        """Tests inheritance"""

        self.assertTrue(isinstance(self.obj, Amenity))
        self.assertTrue(isinstance(self.obj, BaseModel))

    def test_hasattribs(self):
        """Tests that Amenity class has the right public class
        attributes.
        """
        self.assertTrue(hasattr(self.obj, 'name'))

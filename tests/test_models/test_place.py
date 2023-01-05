#!/usr/bin/python3
"""Test suite for Place class"""
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def setUp(self):
        """sets up the tests"""

        self.obj = Place()

    def test_inheritance(self):
        """Tests that the class Place inherits from BaseModel"""

        self.assertTrue(isinstance(self.obj, Place))
        self.assertTrue(isinstance(self.obj, BaseModel))

    def test_hasattr(self):
        """Tests the Place has the right public attributes."""
        
        self.assertTrue(hasattr(self.obj, 'city_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'name'))
        self.assertTrue(hasattr(self.obj, 'description'))
        self.assertTrue(hasattr(self.obj, 'number_rooms'))
        self.assertTrue(hasattr(self.obj, 'number_bathrooms'))
        self.assertTrue(hasattr(self.obj, 'max_guest'))
        self.assertTrue(hasattr(self.obj, 'price_by_night'))
        self.assertTrue(hasattr(self.obj, 'latitude'))
        self.assertTrue(hasattr(self.obj, 'longitude'))
        self.assertTrue(hasattr(self.obj, 'amenity_ids'))

#!/usr/bin/python3
"""Test suite for Review class."""
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """sets up the tests"""

        self.obj = Review()

    def test_inheritance(self):
        """Tests that BaseModel is a parent class for Review."""

        self.assertTrue(isinstance(self.obj, Review))
        self.assertTrue(isinstance(self.obj, BaseModel))

    def test_hasattributes(self):
        """Tests that Review has the right public class attributes"""

        self.assertTrue(hasattr(self.obj, 'place_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'text'))

    def test_attr_values(self):
        """Tests default values for attributes."""

        self.assertEqual(self.obj.place_id, '')
        self.assertEqual(self.obj.user_id, '')
        self.assertEqual(self.obj.text, '')

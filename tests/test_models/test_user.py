#!/usr/bin/python3
"""Test module for User."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the class User."""

    def setUp(self):
        """sets up the test cases."""
        self.obj = User()

    def test_parent(self):
        """Tests inheritance of class BaseModel."""
        self.assertTrue(isinstance(self.obj, BaseModel))

    def test_has_attributes(self):
        """Tests the attributes of the User class."""

        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))

    def test_attr(self):
        """Test empty values for public User class attributes."""

        self.assertEqual(self.obj.email, '')
        self.assertEqual(self.obj.password, '')
        self.assertEqual(self.obj.first_name, '')
        self.assertEqual(self.obj.last_name, '')

        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')
        self.assertEqual(User.first_name, '')
        self.assertEqual(User.last_name, '')

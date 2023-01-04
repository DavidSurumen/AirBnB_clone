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

    def test_inheritance(self):
        """Tests inheritance of class BaseModel."""
        self.assertTrue(isinstance(self.obj, BaseModel))

    def test_has_attributes(self):
        """Tests the attributes of the User class."""

        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))

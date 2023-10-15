#!/usr/bin/python3
"""Test case for the User class"""
import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up the test for testing users."""
        self.user = User()
        self.user.email = "test@test.com"
        self.user.first_name = "Test"
        self.user.last_name = "User"
        self.user.password = "test1234"


    def tearDown(self):
        """Tears down the test."""
        del self.user

    def test_init(self):
        """Test the default initialization of user."""
        self.assertTrue(isinstance(self.user, User))

    def test_attributes(self):
        """Test that User has the required attributes."""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_created_at(self):
        """Test that created_at is assigned correctly."""
        self.assertTrue(isinstance(self.user.created_at, datetime))

    def test_updated_at(self):
        """Test that updated_at is updated correctly."""
        old_time = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_time)

    def test_to_dict(self):
        """Test the conversion of user object attributes to dictionary."""
        user_dict = self.user.to_dict()
        self.assertEqual(self.user.__class__.__name__, "User")
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["id"], self.user.id)
        self.assertEqual(user_dict["created_at"], self.user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], self.user.updated_at.isoformat())
        self.assertEqual(user_dict["email"], self.user.email)
        self.assertEqual(user_dict["password"], self.user.password)
        self.assertEqual(user_dict["first_name"], self.user.first_name)
        self.assertEqual(user_dict["last_name"], self.user.last_name)

    def test_str_representation(self):
        """Test the string representation of the User class."""
        expected = "[{}] ({}) {}".format(self.user.__class__.__name__, self.user.id, self.user.__dict__)
        self.assertEqual(expected, str(self.user))

if __name__ == "__main__":
    unittest.main()

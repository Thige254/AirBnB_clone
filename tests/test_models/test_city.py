#!/usr/bin/python3
"""Unit tests for city.py"""

import unittest
from datetime import datetime
from models import city
from models.city import City

class TestCity(unittest.TestCase):
    """Tests for City class."""

    def setUp(self):
        """Set up tests."""
        self.city = City()

    def tearDown(self):
        """Tear down test."""
        del self.city

    def test_attributes(self):
        """Test attributes exist."""
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_type_attributes(self):
        """Test type of attributes."""
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary."""
        city_dict = self.city.to_dict()
        self.assertEqual(self.city.__class__.__name__, 'City')
        self.assertEqual(city_dict["__class__"], 'City')
        self.assertEqual(city_dict["id"], self.city.id)
        self.assertEqual(city_dict["created_at"], self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], self.city.updated_at.isoformat())

    def test_str(self):
        """Test string representation of object."""
        city_str = str(self.city)
        self.assertEqual(city_str, "[City] ({}) {}".format(self.city.id, self.city.__dict__))

    def test_from_dict(self):
        """Test creating an object from a dictionary."""
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertIsNot(self.city, new_city)
        self.assertEqual(self.city.id, new_city.id)
        self.assertEqual(self.city.created_at, new_city.created_at)
        self.assertEqual(self.city.updated_at, new_city.updated_at)
        self.assertEqual(self.city.name, new_city.name)
        self.assertEqual(self.city.state_id, new_city.state_id)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unit tests for amenity.py"""

import unittest
from datetime import datetime
from models import amenity
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Tests for Amenity class."""

    def setUp(self):
        """Set up tests."""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down test."""
        del self.amenity

    def test_attributes(self):
        """Test attributes exist."""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_type_attributes(self):
        """Test type of attributes."""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertIsInstance(self.amenity.name, str)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(self.amenity.__class__.__name__, 'Amenity')
        self.assertEqual(amenity_dict["__class__"], 'Amenity')
        self.assertEqual(amenity_dict["id"], self.amenity.id)
        self.assertEqual(amenity_dict["created_at"], self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"], self.amenity.updated_at.isoformat())

    def test_str(self):
        """Test string representation of object."""
        amenity_str = str(self.amenity)
        self.assertEqual(amenity_str, "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__))

    def test_from_dict(self):
        """Test creating an object from a dictionary."""
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertIsNot(self.amenity, new_amenity)
        self.assertEqual(self.amenity.id, new_amenity.id)
        self.assertEqual(self.amenity.created_at, new_amenity.created_at)
        self.assertEqual(self.amenity.updated_at, new_amenity.updated_at)
        self.assertEqual(self.amenity.name, new_amenity.name)

if __name__ == "__main__":
    unittest.main()

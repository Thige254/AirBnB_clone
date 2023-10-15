#!/usr/bin/python3
"""Unit tests for place.py"""

import unittest
from datetime import datetime
from models import place
from models.place import Place

class TestPlace(unittest.TestCase):
    """Tests for Place class."""

    def setUp(self):
        """Set up tests."""
        self.place = Place()

    def tearDown(self):
        """Tear down test."""
        del self.place

    def test_attributes(self):
        """Test attributes exist."""
        attributes = ["id", "created_at", "updated_at", "city_id", "user_id", 
                      "name", "description", "number_rooms", "number_bathrooms",
                      "max_guest", "price_by_night", "latitude", "longitude",
                      "amenity_ids"]
        for attr in attributes:
            self.assertTrue(hasattr(self.place, attr))

    def test_type_attributes(self):
        """Test type of attributes."""
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary."""
        place_dict = self.place.to_dict()
        self.assertEqual(self.place.__class__.__name__, 'Place')
        self.assertEqual(place_dict["__class__"], 'Place')
        self.assertEqual(place_dict["id"], self.place.id)
        self.assertEqual(place_dict["created_at"], self.place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"], self.place.updated_at.isoformat())

    def test_str(self):
        """Test string representation of object."""
        place_str = str(self.place)
        self.assertEqual(place_str, "[Place] ({}) {}".format(self.place.id, self.place.__dict__))

    def test_from_dict(self):
        """Test creating an object from a dictionary."""
        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)
        self.assertIsNot(self.place, new_place)
        self.assertEqual(self.place.id, new_place.id)
        self.assertEqual(self.place.created_at, new_place.created_at)
        self.assertEqual(self.place.updated_at, new_place.updated_at)
        self.assertEqual(self.place.name, new_place.name)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unit tests for review.py"""

import unittest
from datetime import datetime
from models import review
from models.review import Review

class TestReview(unittest.TestCase):
    """Tests for Review class."""

    def setUp(self):
        """Set up tests."""
        self.review = Review()

    def tearDown(self):
        """Tear down test."""
        del self.review

    def test_attributes(self):
        """Test attributes exist."""
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_type_attributes(self):
        """Test type of attributes."""
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary."""
        review_dict = self.review.to_dict()
        self.assertEqual(self.review.__class__.__name__, 'Review')
        self.assertEqual(review_dict["__class__"], 'Review')
        self.assertEqual(review_dict["id"], self.review.id)
        self.assertEqual(review_dict["created_at"], self.review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"], self.review.updated_at.isoformat())

    def test_str(self):
        """Test string representation of object."""
        review_str = str(self.review)
        self.assertEqual(review_str, "[Review] ({}) {}".format(self.review.id, self.review.__dict__))

    def test_from_dict(self):
        """Test creating an object from a dictionary."""
        review_dict = self.review.to_dict()
        new_review = Review(**review_dict)
        self.assertIsNot(self.review, new_review)
        self.assertEqual(self.review.id, new_review.id)
        self.assertEqual(self.review.created_at, new_review.created_at)
        self.assertEqual(self.review.updated_at, new_review.updated_at)
        self.assertEqual(self.review.text, new_review.text)

if __name__ == "__main__":
    unittest.main()

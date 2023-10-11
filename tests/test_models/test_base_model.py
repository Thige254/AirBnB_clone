#!/usr/bin/python3
"""Tests for BaseModel"""
import unittest
from datetime import datetime
from models.base_model import BaseModel

# class TestBaseModel that inherits from unittest.TestCase
class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    def setUp(self):
        """Set up method"""
        self.instance = BaseModel()

    def tearDown(self):
        """Tear down method"""
        del self.instance

    def test_id_creation(self):
        """Test that id is correctly created and is a string"""
        self.assertIsInstance(self.instance.id, str)

    def test_datetime_creation(self):
        """Test that created_at and updated_at are created and are datetime objects"""
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel"""
        model_dict = self.instance.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_method(self):
        """Test the __str__ method of BaseModel"""
        expected = "[{}] ({}) {}".format(self.instance.__class__.__name__, self.instance.id, self.instance.__dict__)
        self.assertEqual(expected, str(self.instance))

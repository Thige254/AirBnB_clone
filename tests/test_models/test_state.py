#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State
import datetime
import os


class TestState(unittest.TestCase):
    
    def setUp(self):
        """Set up method before each `test_` method is called."""
        self.state = State()

    def tearDown(self):
        """Clean up after each `test_` method."""
        del self.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_instance(self):
        """Test for instantiation."""
        self.assertTrue(isinstance(self.state, State))
        self.assertTrue(isinstance(self.state, BaseModel))

    def test_attributes(self):
        """Test if attributes exist and are set to the expected default."""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_unique_id(self):
        """Test if an ID is unique."""
        state2 = State()
        self.assertNotEqual(self.state.id, state2.id)

    def test_datetime(self):
        """Test for valid date & time attributes."""
        self.assertEqual(self.state.created_at, self.state.updated_at)
        self.assertTrue(isinstance(self.state.created_at, datetime.datetime))
        self.assertTrue(isinstance(self.state.updated_at, datetime.datetime))

    def test_str_method(self):
        """Test the __str__ method."""
        expected = "[{}] ({}) {}".format(
            self.state.__class__.__name__, self.state.id, self.state.__dict__)
        self.assertEqual(expected, str(self.state))

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary."""
        state_dict = self.state.to_dict()
        self.assertEqual(self.state.__class__.__name__, 'State')
        self.assertEqual(state_dict["__class__"], 'State')
        self.assertEqual(state_dict["id"], self.state.id)
        self.assertEqual(state_dict["created_at"], self.state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], self.state.updated_at.isoformat())

    def test_file_storage(self):
        """Test that object is stored correctly in the file."""
        self.state.save()
        with open('file.json', 'r') as file:
            storage = file.readlines()

        self.assertTrue(len(storage) > 0)

    def test_attr_types(self):
        """Test attribute types."""
        self.assertTrue(type(self.state.name) is str)

    def test_set_attr(self):
        """Test to set an attribute."""
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_save_string_representation(self):
        """Test string representation after calling save."""
        self.state.save()
        with open("file.json", "r") as f:
            saved = f.read()
            self.assertIn("State." + self.state.id, saved)

    # I will add more edge cases or specific scenarios as needed


if __name__ == "__main__":
    unittest.main()

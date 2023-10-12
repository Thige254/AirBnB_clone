#!/usr/bin/python3
#Test cases for city class
import unittest
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_init(self):
        self.assertTrue(isinstance(self.city, City))
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_str_method(self):
        city_str = self.city.__str__()
        self.assertEqual(city_str,
                         "[City] ({}) {}".format(self.city.id, self.city.__dict__))

    def test_save(self):
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(type(city_dict["created_at"]), str)
        self.assertEqual(type(city_dict["updated_at"]), str)

    def test_name_attr(self):
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_set_attr(self):
        """Test to set attributes"""
        self.city.name = "San Francisco"
        self.city.state_id = "CA_12345"
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.state_id, "CA_12345")

    # additional edge cases to be added here...

if __name__ == "__main__":
    unittest.main()

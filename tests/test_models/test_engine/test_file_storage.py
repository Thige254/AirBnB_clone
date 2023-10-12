#!/usr/bin/python3
# Test case for the file_storage class
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Sets up the test for potential file creation."""
        self.storage = FileStorage()  # Create a new instance of FileStorage for testing
        self.file_path = "test.json"  # Define the file_path for testing
        if not os.path.exists(self.file_path):  # If the test file doesn't exist, create an empty one
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write("{}")

    def tearDown(self):
        """Removes the file after test."""
        try:
            os.remove(self.file_path)
        except:
            pass

    def test_all(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        all_objs = self.storage.all()
        self.assertTrue(obj_key in all_objs)

    def test_new(self):
        obj = User()
        self.storage.new(obj)
        all_objs = self.storage.all()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertTrue(obj_key in all_objs)
        self.assertTrue(obj_key in self.storage.all())

    def test_save(self):
        """Tests the save method."""
        obj = BaseModel()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, "r", encoding="utf-8") as f:
            json_objs = f.read()
            print(f"Json Objects: {json_objs}")  #see the content of the file after saving
            print(f"Expected Key: {obj_key}")    # check the key
            self.assertTrue(obj_key in json_objs)


    def test_reload(self):
        obj = User()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        all_objs = self.storage.all()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertTrue(obj_key in all_objs)

    def test_invalid_reload(self):
        """Tests reloading from an invalid file."""
        obj_count_before = len(self.storage.all())
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
        self.storage.reload()
        obj_count_after = len(self.storage.all())
        self.assertEqual(obj_count_before, obj_count_after)  # Ensure that the number of objects remains the same

    def test_invalid_class_reload(self):
        """Tests reloading with an undefined class."""
        obj_count_before = len(self.storage.all())
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write('{"InvalidClass.12345": {"id": "12345", "__class__": "InvalidClass"}}')
        self.storage.reload()
        obj_count_after = len(self.storage.all())
        self.assertEqual(obj_count_before, obj_count_after)  # Ensure that the number of objects remains the same

if __name__ == "__main__":
    unittest.main()

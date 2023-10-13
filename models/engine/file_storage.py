#!/usr/bin/python3
"""
FileStorage class for AirBnB project
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        # Dictionary of all classes available for the FileStorage
        classes = {
            "BaseModel": BaseModel, 
            "User": User, 
            "State": State, 
            "City": City, 
            "Amenity": Amenity, 
            "Place": Place, 
            "Review": Review
        }

        # an addition (We might delete it. There is something i am testing):
        #This method returns a dictionary where the keys are the names of the model classes and the values
        # are lists of the attributes that instances of each class should have

    def attributes(self):
        """Return the attributes for each model class."""
        class_attributes = {
            "BaseModel": ["id", "created_at", "updated_at"],
            "User": ["id", "email", "password", "first_name", "last_name", "created_at", "updated_at"],
            "State": ["id", "name", "created_at", "updated_at"],
            "City": ["id", "state_id", "name", "created_at", "updated_at"],
            "Amenity": ["id", "name", "created_at", "updated_at"],
            "Place": ["id", "city_id", "user_id", "name", "description", "number_rooms", "number_bathrooms", "max_guest", "price_by_night", "latitude", "longitude", "amenity_ids", "created_at", "updated_at"],
            "Review": ["id", "place_id", "user_id", "text", "created_at", "updated_at"]
        }
        return class_attributes
       
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name in classes:  # Safety check
                        cls = classes[class_name]
                        instance = cls(**value)  # Create a new instance
                        FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass

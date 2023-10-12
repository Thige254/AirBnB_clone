#!/usr/bin/python3
# mode for FileStorage class of AirBnB project
"""
FileStorage class for AirBnB project
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    # To avoid errors i was getting, i will keep the class names
    # for now and will dynamically import them later.
    __class_dict = {
        "BaseModel": "BaseModel",
        "User": "User"
        # For future... additional classes, include them here:
        # "OtherModel": "OtherModel"
    }

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value.pop("__class__", None)  # This change ensures __class__ is removed
                    if class_name in self.__class_dict:
                        # Dynamically importing the required model class
                        mod = __import__('models.' + class_name, fromlist=[class_name])
                        cls = getattr(mod, class_name)
                        instance = cls(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass

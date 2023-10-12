#!/usr/bin/python3
"""The base model script"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for the BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                # if `key` is `__class__`, skip it
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    setattr(
                        self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                    )
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # set new instance in the `__objects` dict for storage
            models.storage.new(self)

    def __str__(self):
        """String representation of BaseModel."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict

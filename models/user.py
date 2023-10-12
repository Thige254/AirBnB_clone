#!/usr/bin/python3
"""The user module that creates a (user) class"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel & manages user objects."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

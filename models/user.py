#!/usr/bin/python3
"""The user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """The class user that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3
"""The review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

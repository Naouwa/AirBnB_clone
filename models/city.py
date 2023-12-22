#!/usr/bin/python3
"""The city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """The City class(child) that inherits from BaseModel(parent)"""
    state_id = ""
    name = ""

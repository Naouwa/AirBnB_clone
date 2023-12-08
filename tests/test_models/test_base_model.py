#!/usr/bin/python3
"""Unittests for base_model.py"""

import models
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instance_creation(self):
        """Test instance creation"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)


if __name__ == '__main__':
    unittest.main()

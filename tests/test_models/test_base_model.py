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

    def test_id_generation(self):
        """Test ID gereration"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_updated_at(self):
        """Test created_at and updated_at attributes"""
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save_method(self):
        """Test the save method"""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertTrue(isinstance(instance_dict, dict))
        self.assertIn("__class__", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)


if __name__ == '__main__':
    unittest.main()

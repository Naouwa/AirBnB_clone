#!/usr/bin/python3
"""Unittests for models/engine/filestorage.py"""
import unittest
import models
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class Test_FileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def test_FileStorage_inst(self):
        """Test FileStorage regular instantiation"""
        self.assertEqual(type(FileStorage()), FileStorage)
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_filepath(self):
        """Test cases for __file_path"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_docs(self):
        """Test for FileStorage doctring"""
        self.assertIsNotNone(FileStorage.__doc__)


if __name__ == "__main__":
    unittest.main()

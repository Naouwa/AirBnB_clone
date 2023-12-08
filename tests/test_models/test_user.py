#!/usr/bin/python3
"""Unittests for models/usr.py"""
import unittest
import models
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import os
from time import sleep


class TestUser(unittest.TestCase):
    """User class test cases"""

    def setUp(self):
        """setup function for test"""

        self.user = User()
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """unittest teardown"""

        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_docstr(self):
        """tests doctrings exist"""

        self.assertIsNotNone(User.__doc__)

    def test_is_sub(self):
        """Test User inheriting from BaseModel"""

        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_attributes(self):
        """Test User has all attributes"""

        user = User(email="at", password="code")
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_attr_str(self):
        """Test attributes type is string"""

        user = User()
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_dates(self):
        """Tests user attr using datetime"""
        user = User()
        self.assertEqual(datetime, type(self.user.created_at))
        self.assertEqual(datetime, type(self.user.updated_at))

    def test_uid(self):
        """Tests regular cases"""
        user1 = User()
        sleep(0.08)
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)
        self.assertNotEqual(user1.created_at, user2.created_at)
        self.assertNotEqual(user1.updated_at, user2.updated_at)

    def test_unused(self):
        """Tests case of unused arguments"""
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_save(self):
        """Tests save method for User"""

        user = User()
        sleep(0.08)
        update = user.updated_at
        user.save()
        self.assertLess(update, user.updated_at)

    def test_save_arg(self):
        """Tests multiple save method for User"""

        user = User()
        with self.assertRaises(TypeError):
            user.save("hello")

    def test_file_update(self):
        """Tests if file updates after save"""

        user = User()
        user.save()
        user.save()
        uid = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(uid, f.read())

    def test_dict(self):
        """Tests to_dict method for User"""
        user = User()
        self.assertTrue(dict, type(user.to_dict()))
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_add_dict(self):
        """Tests added attributes to instance of User"""
        user = User()
        user.postal = "20000"
        self.assertEqual("20000", user.postal)
        self.assertIn("postal", user.to_dict())


if __name__ == '__main__':
    unittest.main()

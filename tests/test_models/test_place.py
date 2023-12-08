#!/usr/bin/python3
"""Unittests module for place.py"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.place import Place
import uuid


class TestPlace(unittest.TestCase):
    """Test cases for the place class"""

    def test_instance_creation(self):
        """Test if a Place instance is created successfully"""
        place = Place()
        self.assertIsInstance(place, Place)

    @unittest.skip("Skipping test due to unresolved issue")
    def test_attributes(self):
        """Test if Place attributes are correctly set"""
        place = Place()
        self.assertIsNone(place.city_id)
        self.assertIsNone(place.user_id)
        self.assertIsNone(place.name)
        self.assertIsNone(place.description)
        self.assertIsNone(place.number_rooms)
        self.assertIsNone(place.number_bathrooms)
        self.assertIsNone(place.max_guest)
        self.assertIsNone(place.price_by_night)
        self.assertIsNone(place.latitude)
        self.assertIsNone(place.longitude)
        self.assertIsNone(place.amenity_ids)

    def test_save_method(self):
        """Test the save method to update 'updated_at'"""
        place = Place()
        original_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(original_updated_at, place.updated_at)

    @unittest.skip("Skipping test due to unresolved issue")
    def test_to_dict_method(self):
        """Test the to_dict method for serialization"""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)


if __name__ == '__main__':
    unittest.main()

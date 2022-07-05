#!/usr/bin/python3
"""Unit test for Amenity class"""

from models.base_model import BaseModel
from os.path import exists
import unittest


class Test_BaseModel(unittest.TestCase):
    """Base_model test"""

    def test_created_at(self):
        """Test created_at"""
        obj = BaseModel()
        self.assertEqual(obj.created_at(), None)

    def test_updated_at(self):
        """Test updated_at"""
        obj = BaseModel()
        self.assertEqual(obj.updated_at(), None)

    def test_to_dict(self):
        """Test todict method"""
        obj = BaseModel()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        self.assertEqual(obj.save(), None)

    def test_id(self):
        """Test id"""
        obj = BaseModel()
        self.assertEqual(type(obj.id), str)

    def test_str(self):
        """ test __str__ return value type """
        obj = BaseModel()
        self.assertEqual(type(obj.__str__()), str)

    if __name__ == "__main__":
        unittest.main()

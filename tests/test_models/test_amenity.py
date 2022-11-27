#!/usr/bin/python3
"""Module for testing Amenity model"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.amenity = Amenity(name='dummy')

    def test_name2(self):
        """ """
        self.assertEqual(type(self.amenity.name), str)

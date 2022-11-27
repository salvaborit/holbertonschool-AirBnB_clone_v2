#!/usr/bin/python3
"""Module for testing Place model"""


from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.place = Place(city_id='dummy',
                           user_id='dummy',
                           name='dummy',
                           description='dummy',
                           number_rooms=4,
                           number_bathrooms=4,
                           max_guest=4,
                           price_by_night=100,
                           latitude=35.35,
                           longitude=32.32)

    def test_city_id(self):
        """ """
        self.assertEqual(type(self.place.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.place.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.place.name), str)

    def test_description(self):
        """ """
        self.assertEqual(type(self.place.description), str)

    def test_number_rooms(self):
        """ """
        self.assertEqual(type(self.place.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.assertEqual(type(self.place.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.assertEqual(type(self.place.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.assertEqual(type(self.place.price_by_night), int)

    def test_latitude(self):
        """ """
        self.assertEqual(type(self.place.latitude), float)

    def test_longitude(self):
        """ """
        self.assertEqual(type(self.place.latitude), float)

    def test_amenity_ids(self):
        """ """
        self.assertEqual(type(self.place.amenity_ids), list)

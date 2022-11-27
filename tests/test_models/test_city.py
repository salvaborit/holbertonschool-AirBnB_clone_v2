#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.city = City(name='Miami', state_id='dummy')

    def test_state_id(self):
        """ """
        self.assertEqual(type(self.city.state_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.city.name), str)

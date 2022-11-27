#!/usr/bin/python3
"""Module for testing State model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.state = State(name='Florida')

    def test_name3(self):
        """ """
        self.assertEqual(type(self.state.name), str)

#!/usr/bin/python3
"""Module for testing Review model"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.review = Review(text='dummy', place_id='dummy', user_id='dummy')

    def test_place_id(self):
        """ """
        self.assertEqual(type(self.review.place_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.review.user_id), str)

    def test_text(self):
        """ """
        self.assertEqual(type(self.review.text), str)

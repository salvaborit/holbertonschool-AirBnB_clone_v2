#!/usr/bin/python3
"""Module for testing User model"""


from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def setUp(self):
        """ """
        self.user = User(email='sba@hbtn.com', password='pwd',
                         first_name='Salvador', last_name='Borit')

    def test_first_name(self):
        """ """
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name(self):
        """ """
        self.assertEqual(type(self.user.last_name), str)

    def test_email(self):
        """ """
        self.assertEqual(type(self.user.email), str)

    def test_password(self):
        """ """
        self.assertEqual(type(self.user.password), str)

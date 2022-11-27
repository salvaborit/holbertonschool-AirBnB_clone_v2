#!/usr/bin/python3
"""Module with console unittests"""


import unittest
import console


class TestConsole(unittest.TestCase):
    """Class that tests console"""

    def test_emptyline(self):
        console_test = console.HBNBCommand
        self.assertTrue(console_test("\n"), 'pass')

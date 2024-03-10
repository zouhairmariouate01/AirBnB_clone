#!/usr/bin/env python3

import datetime
import unittest
from models.city import City

"""
    test_city Module.
"""


class test_city(unittest.TestCase):
    """
        Class of test_city.
        To tests the unit of instance's attributes.
    """

    def test_0_instantiation(self):
        """
            Method to tests the instantiation from
            class of City.
        """

        ins = City()
        self.assertIsNotNone(ins)
        self.assertIsInstance(ins, City)
        self.assertEqual(type(ins), City)

    def test_1_initialisation(self):
        """
            Method to tests the initialisation of attributes.
        """

        ins = City()
        ins.name = "city name"
        self.assertEqual(ins.name, "city name")
        ins.state_id = "state id"
        self.assertEqual(ins.state_id, "state id")

    def test_2_id(self):
        """
            Method that tests the id of instance.
        """

        ins = City()
        self.assertIsNotNone(ins.id)
        self.assertIsInstance(ins.id, str)

    def test_3_changing_types(self):
        """
            Method that tests changing the types
            of attributes.
        """

        ins = City()
        ins.name = []
        ins.state_id = 10
        self.assertIsInstance(ins.name, list)
        self.assertIsInstance(ins.state_id, int)


if __name__ == '__main__':
    unittest.main()

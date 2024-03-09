#!/usr/bin/env python3

import unittest
import datetime
from models.amenity import Amenity

"""
    test_amenity Module.
"""


class test_amenity(unittest.TestCase):
    """
        test_amenity Class.
        To tests the unit of class Amenity.
    """

    def test_0_instantiation(self):
        """
            Method to test the instantiation
            from Amenity class.
        """

        ins = Amenity()
        self.assertIsNotNone(ins)
        self.assertIsInstance(ins, Amenity)
        self.assertEqual(type(ins), Amenity)

    def test_1_initialisation(self):
        """
            Method to tests the initialisation of attributes.
        """

        ins = Amenity()
        ins.name = "name"
        self.assertEqual(ins.name, "name")

    def test_2_id(self):
        """
            Method that tests the id of instance.
        """

        ins = Amenity()
        self.assertIsNotNone(ins.id)
        self.assertIsInstance(ins.id, str)

    def test_3_changing_types(self):
        """
            Method that tests changing the types
            of attributes.
        """

        ins = Amenity()
        ins.name = []
        self.assertIsInstance(ins.name, list)


if __name__ == '__main__':
    unittest.main()

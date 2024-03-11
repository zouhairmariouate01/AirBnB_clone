#!/usr/bin/env python3

import unittest
import datetime
from models.place import Place

"""
    Module of test_place.
"""


class test_place(unittest.TestCase):
    """
        Class of test_place.
        To tests the units of instance's attributes.
    """

    def test_0_instantiation(self):
        """
            Method that tests the instantiation new objects
            from Place class.
        """

        ins = Place()
        self.assertIsNotNone(ins)
        self.assertIsInstance(ins, Place)
        self.assertEqual(type(ins), Place)

    def test_1_initialisation(self):
        """
            Method that tests the initialisation of attributes
            of the object.
        """

        ins = Place()
        ins.name = "name"
        self.assertEqual(ins.name, "name")
        ins.description = "test"
        self.assertEqual(ins.description, "test")
        ins.city_id = "id"
        self.assertEqual(ins.city_id, "id")
        ins.user_id = "id"
        self.assertEqual(ins.user_id, "id")
        ins.number_rooms = 10
        self.assertEqual(ins.number_rooms, 10)
        ins.number_bathrooms = 10
        self.assertEqual(ins.number_bathrooms, 10)
        ins.max_guest = 10
        self.assertEqual(ins.max_guest, 10)
        ins.price_by_night = 10
        self.assertEqual(ins.price_by_night, 10)
        ins.latitude = 10.01
        self.assertEqual(ins.latitude, 10.01)
        ins.amenity_ids = [10, 20]
        self.assertEqual(ins.amenity_ids, [10, 20])

    def test_2_id(self):
        """
            Method that test the id of instance.
        """

        ins = Place()
        self.assertIsNotNone(ins.id)
        self.assertIsInstance(ins.id, str)
        self.assertNotEqual(ins.id, "")

    def test_3_changing_types(self):
        """
            Method that tests changing the types of
            instance's attributes.
        """

        ins = Place()
        ins.name = []
        ins.amenity_ids = ""
        ins.description = 11
        ins.latitude = {}
        ins.longitude = 0.1
        self.assertIsInstance(ins.name, list)
        self.assertIsInstance(ins.amenity_ids, str)
        self.assertIsInstance(ins.description, int)
        self.assertIsInstance(ins.latitude, dict)
        self.assertIsInstance(ins.longitude, float)

    def test_4_creation_date(self):
        """
            Method that tests the date of creation.
        """

        ins = Place()
        self.assertIsNotNone(ins.created_at)
        self.assertIsInstance(ins.created_at, datetime.datetime)

    def test_5_update_date(self):
        """
            Method that tests the date of update.
        """

        ins = Place()
        self.assertIsNotNone(ins.updated_at)
        self.assertIsInstance(ins.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

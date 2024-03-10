#!/usr/bin/env python3

import unittest
import datetime
from models.review import Review

"""
    test_review Module.
"""


class test_review(unittest.TestCase):
    """
        test_review class.
        To Do unit tests for the Review class.
    """

    def test_0_instantiation(self):
        """
            Method that tests the instantiation
            from Review class.
        """

        ins = Review()
        self.assertIsNotNone(ins)
        self.assertIsInstance(ins, Review)
        self.assertEqual(type(ins), Review)

    def test_1_initialisation(self):
        """
            Method that tests the initialisation of
            instance's attributes.
        """

        ins = Review()
        self.assertEqual(ins.text, "")
        self.assertEqual(ins.place_id, "")
        self.assertEqual(ins.user_id, "")
        ins.text = "Text"
        self.assertIsNotNone(ins.text)
        self.assertEqual(ins.text, "Text")
        ins.user_id = "User Id"
        self.assertIsNotNone(ins.user_id)
        self.assertEqual(ins.user_id, "User Id")
        ins.place_id = "Place Id"
        self.assertIsNotNone(ins.place_id)
        self.assertEqual(ins.place_id, "Place Id")

    def test_2_equality(self):
        """
            Method that tests the equality of instance's attributes.
        """

        ins = Review()
        self.assertEqual(ins.text, "")
        self.assertEqual(ins.place_id, "")
        self.assertEqual(ins.user_id, "")

    def test_3_id(self):
        """
            Method that tests the instance id.
        """

        ins = Review()
        self.assertIsNotNone(ins.id)
        self.assertIsInstance(ins.id, str)

    def test_4_creation_date(self):
        """
            Method that test the date of creation.
        """

        ins = Review()
        self.assertIsNotNone(ins.created_at)
        self.assertIsInstance(ins.created_at, datetime.datetime)

    def test_5_update_date(self):
        """
            Method that tests the date of update.
        """

        ins = Review()
        self.assertIsNotNone(ins.updated_at)
        self.assertIsInstance(ins.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3

from models.state import State
import unittest
import datetime

"""
    test_state Module.
"""


class test_state(unittest.TestCase):
    """
        test_state Class.
        To Do unit test for the class State.
    """

    def test_0_instantiation(self):
        """
            Method that test the instantiation from
            class of State.
        """

        ins = State()
        self.assertIsNotNone(ins)
        self.assertIsInstance(ins, State)
        self.assertEqual(type(ins), State)

    def test_1_initialisation(self):
        """
            Method that test the initialisation from
            class State.
        """

        ins = State()
        ins.name = "Name"
        self.assertEqual(ins.name, "Name")

    def test_2_changing_types(self):
        """
            Method that checks changing data types.
        """

        ins = State()
        self.assertIsInstance(ins.name, str)
        ins.name = []
        self.assertIsInstance(ins.name, list)
        ins.name = {}
        self.assertIsInstance(ins.name, dict)
        ins.name = 0
        self.assertIsInstance(ins.name, int)
        ins.name = 1.0005
        self.assertIsInstance(ins.name, float)
        ins.name = True
        self.assertIsInstance(ins.name, bool)

    def test_3_equality(self):
        """
            Method that tests the equality of attributes.
        """

        ins = State()
        self.assertEqual(ins.name, "")

    def test_4_creation_date(self):
        """
            Method that tests the date of creation.
        """

        ins = State()
        self.assertIsNotNone(ins.created_at, None)
        self.assertIsInstance(ins.created_at, datetime.datetime)

    def test_5_update_date(self):
        """
            Method that tests the date of update.
        """

        ins = State()
        self.assertIsNotNone(ins.updated_at, None)
        self.assertIsInstance(ins.updated_at, datetime.datetime)

    def test_6_id(self):
        """
            Method that tests the instance id.
        """

        ins = State()
        self.assertIsNotNone(ins.id)
        self.assertIsInstance(ins.id, str)


if __name__ == '__main__':
    unittest.main()

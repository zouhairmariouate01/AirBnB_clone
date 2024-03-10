#!/usr/bin/env python3

from models.user import User
import unittest

"""
    test_user Module.
"""


class test_user(unittest.TestCase):
    """
        test_user Class.
        To Do Unit Test for the User class.
    """

    def test_0_instantiation(self):
        """
            Method to test the instantiation from User class.
        """

        instance = User()
        self.assertIsInstance(instance, User)
        self.assertFalse(instance is None)
        self.assertEqual(type(instance), User)

    def test_1_equality(self):
        """
            Method that tests the initailisation of attributes
            with values.
        """

        instance = User()
        self.assertEqual(instance.first_name, "")
        self.assertEqual(instance.last_name, "")
        self.assertEqual(instance.password, "")
        self.assertEqual(instance.email, "")

    def test_2_types(self):
        """
            Method that tests the types of attributes.
        """

        instance = User()
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.last_name, str)
        self.assertIsInstance(instance.password, str)
        self.assertIsInstance(instance.email, str)

    def test_3_initialisation(self):
        """
            Method that tests the initialisation of attributes.
        """

        instance = User()
        instance.first_name = "First Name"
        self.assertEqual(instance.first_name, "First Name")
        instance.last_name = "Last Name"
        self.assertEqual(instance.last_name, "Last Name")
        instance.email = "Email"
        self.assertEqual(instance.email, "Email")
        instance.password = "Password"
        self.assertEqual(instance.password, "Password")

    def test_4_change_types(self):
        """
            Method that tests entring different data types
            to the instance's attributes.
        """

        instance = User()
        instance.first_name = {}
        self.assertIsInstance(instance.first_name, dict)
        instance.last_name = 15
        self.assertIsInstance(instance.last_name, int)
        instance.email = []
        self.assertIsInstance(instance.email, list)
        instance.password = 15.001
        self.assertIsInstance(instance.password, float)

    def test_5_id(self):
        """
            Method that tests the id of instance.
        """

        ins = User()
        self.assertIsInstance(ins.id, str)
        self.assertIsNotNone(ins.id)
        self.assertNotEqual(ins.id, "")


if __name__ == '__main__':
    unittest.main()

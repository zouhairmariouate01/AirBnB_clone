#!/usr/bin/env python3

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

"""
    test_file_storage module of Unittest.
"""


class test_file_storage(unittest.TestCase):
    """
        class TestFileStorage.

        Usage:
            class used to test the units of class FileStorage.
    """
    instance = None

    def test_0_instantiation(self):
        """
            Method for testing the instantiation.
        """
        test_file_storage.instance = FileStorage()
        self.assertIsInstance(test_file_storage.instance, FileStorage)
        self.assertTrue(
            str(type(test_file_storage.instance)) ==
            "<class 'models.engine.file_storage.FileStorage'>"
        )

    def test_1_initilisation(self):
        """
            Method for testing the insialisation of instance
            with some data.
        """
        model = BaseModel()
        model.name = "This is test"
        model.number = 11
        model.save()
        self.assertIsNotNone(test_file_storage.instance)

    def test_2_storing_objects(self):
        """
            Method tests the storage of objects.
        """
        self.assertFalse(test_file_storage.instance.all() == {})

    def test_3_json_files_creation(self):
        """
            Method tests the creation of JSON files.
        """
        self.assertTrue(os.path.exists("file.json"))

    def test_4_deserialisation(self):
        """
            Method tests desertialisation of objects from
            JSON file.
        """
        test_file_storage.instance = None
        test_file_storage.instance = FileStorage()
        test_file_storage.instance.reload()
        self.assertNotEqual(test_file_storage.instance.all(), {})


if __name__ == '__main__':
    unittest.main()

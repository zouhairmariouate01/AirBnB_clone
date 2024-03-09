#!/usr/bin/env python3

from console import HBNBCommand
import unittest
from unittest.mock import patch
from io import StringIO

"""
    test_console Module.
    For testing the HBNBCommand console with unittest.
"""


class test_HBNBCommand(unittest.TestCase):
    """
        test_HBNBCommand class.
    """
    def test_0_prompt(self):
        """
            Method used to test prompting of the console.
        """
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_1_empty_line(self):
        """
            Method used to test entring an empty line
            to the console prompt.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_2_help(self):
        """
            Method to test the help command on console.
        """
        text = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(text, output.getvalue().strip())

    def test_3_EOF(self):
        """
            Method to test the EOF command on console.
        """
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_4_quit(self):
        """
            Method to test the quit command on console.
        """
        self.assertTrue(HBNBCommand().onecmd("quit"))

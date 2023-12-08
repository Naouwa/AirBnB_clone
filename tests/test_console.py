#!/usr/bin/python3
"""Unittests for console.py"""
import unittest
import os
import sys
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class Test_Console(unittest.TestCase):
    """Tests Console cases"""

    def test_prompt(self):
        """Tests console prompt"""

        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == "__main__":
    unittest.main()

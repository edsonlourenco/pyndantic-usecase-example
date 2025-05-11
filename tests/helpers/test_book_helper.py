import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

import unittest
from helpers.book import BookHelper

class TestBookHelper(unittest.TestCase):
    """
    A test class to validate the functionality of BookHelper.

    This class contains unit tests that validate the behavior of methods in the
    BookHelper class. It checks for correct functionality by asserting various
    conditions using the unittest library.
    """

    def test_get_json_path_exists(self):
        """
        Tests the existence of the JSON file path.

        This function verifies whether the file path returned by the `get_json_path`
        method of the `BookHelper` class exists in the filesystem. It uses an assertion
        to ensure that the file path exists.

        Parameters:
            self (TestClass): The instance of the test class where this method is
            implemented.
        """

        path = BookHelper.get_json_path()
        print(path)

        self.assertTrue(os.path.exists(path), f"File do not exist on the path: {path}")

if __name__ == '__main__':
    unittest.main()
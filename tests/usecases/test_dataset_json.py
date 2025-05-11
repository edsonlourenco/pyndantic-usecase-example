import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

import unittest
import json
from schemas.book import Book
from helpers.book import BookHelper

class TestDatasetJSON(unittest.TestCase):
    """
    A unit test class for validating the loading and structure of a JSON dataset.

    This class is designed to ensure that a JSON dataset is properly loaded and
    validated against specific criteria. The tests include checking the existence
    of the JSON file, validating its content length, ensuring proper data
    structures, and confirming compatibility with the `Book` model.
    """

    def test_load_and_validate_json_dataset(self):
        """
        Tests the loading and validation of a JSON dataset for the Book model, verifying
        the integrity of the dataset and ensuring correct deserialization into the model.

        Raises
        ------
        AssertionError
            If the JSON file does not exist, the dataset does not have the expected number
            of items, or any item cannot be validated or deserialized into the Book model.
        """

        # Path to the generated JSON file
        json_path = BookHelper.get_json_path()

        # Check if the file exists
        self.assertTrue(os.path.exists(json_path), f"File not found: {json_path}")

        # Load the JSON content from the file
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Verify the dataset contains 1000 items
        self.assertEqual(len(data), 1000, "Dataset should contain 1000 items.")

        # Validate each item can be loaded into the Book model
        for item in data:
            book = Book.model_validate_json(json.dumps(item))
            self.assertIsInstance(book, Book)

        # Optional: check attributes of the first item
        first_item = data[0]
        self.assertIn('_id', first_item)
        self.assertIn('title', first_item)
        self.assertIn('authors', first_item)
        self.assertIsInstance(first_item['authors'], list)

if __name__ == '__main__':
    unittest.main()

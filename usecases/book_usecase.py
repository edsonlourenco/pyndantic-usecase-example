import pathlib
import csv
import json
from helpers.book import BookHelper as Book_Helper
from schemas.book import Book
from typing import List, Optional
from pydantic import ValidationError

class BookUseCase:
    """
    Handles operations related to processing book data from various sources.

    This class is responsible for reading and converting book information from JSON
    and CSV data into a list of `Book` objects. It includes helper methods for
    processing specific fields like dates, authors, and categories. The class
    aims to enable streamlined book data extraction and transformation for further
    application use.
    """

    def read_from_json(self, limit: Optional[int] = None) -> List[Book]:
        """
        Reads and returns a list of books from a JSON file. The method deserializes the
        book data from a JSON string, validates it, and converts it into `Book`
        instances. Optionally limits the number of books returned.

        Args:
            limit (Optional[int]): The maximum number of books to return. Defaults
            to None, meaning all books will be returned.

        Returns:
            List[Book]: A list of `Book` instances created from the JSON data.
        """
        json_string = pathlib.Path(Book_Helper.get_json_path()).read_text()
        books_data = json.loads(json_string)
        validated_books = [Book(**book_data) for book_data in books_data]
        if limit is not None:
            return validated_books[:limit]
        return validated_books

    def read_from_csv(self, limit: Optional[int] = None) -> List[Book]:
        """
        Reads books data from a CSV file and returns a list of Book objects. The function processes
        each row in the CSV file to extract and parse book data, handling potential parsing
        and validation errors for individual rows.

        Arguments:
            limit (Optional[int]): An optional integer specifying the maximum number
                                   of books to retrieve. If not provided, all books
                                   will be returned.

        Returns:
            List[Book]: A list of Book objects created from the CSV file data.
        """
        csv_path = Book_Helper.get_csv_path()
        books = []
        with open(csv_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    book_data = {
                        "title": row.get("Title"),
                        "isbn": row.get("ISBN"),
                        "pageCount": int(row.get("PageCount")) if row.get("PageCount") else None,
                        "publishedDate": self._parse_date(row.get("PublishedDate")) if row.get("PublishedDate") else None,
                        "thumbnailUrl": row.get("ThumbnailUrl"),
                        "shortDescription": row.get("ShortDescription"),
                        "longDescription": row.get("LongDescription"),
                        "status": row.get("Status"),
                        "authors": self._parse_authors(row.get("Authors")),
                        "categories": self._parse_categories(row.get("Categories")),
                    }
                    book = Book(**book_data)
                    books.append(book)
                except ValueError as e:
                    print(f"Erro ao processar linha CSV: {row} - {e}")
                except ValidationError as e:
                    print(f"Erro de validação Pydantic na linha CSV: {row} - {e}")

        if limit is not None:
            return books[:limit]
        return books

    def _parse_date(self, date_string: str):
        """
        Parses a given date string into ISO 8601 format. This function supports two date
        formats: 'YYYY-MM-DD' and 'YYYY-MM-DDTHH:MM:SS.sssZ'. If the given date string
        does not match any of the supported formats, the function returns None.

        Parameters:
            date_string (str): The date string to parse. Should match one of the
                supported date formats.

        Returns:
            str or None: The parsed date in ISO 8601 format if successful, or None
            if the date string cannot be parsed.
        """
        from datetime import datetime
        try:
            return datetime.strptime(date_string, '%Y-%m-%d').isoformat()
        except ValueError:
            try:
                return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ').isoformat()
            except ValueError:
                return None

    def _parse_authors(self, authors_string: str) -> List[str]:
        """
        Parses a string of authors into a list of individual authors.

        This method takes a string containing multiple authors separated by commas
        and returns a list with individual author names stripped of whitespace.

        Parameters:
            authors_string (str): A comma-separated string of author names.

        Returns:
            List[str]: A list of individual author names.
        """
        if authors_string:
            return [author.strip() for author in authors_string.split(',')]
        return []

    def _parse_categories(self, categories_string: str) -> List[str]:
        """
        Parses a string of categories into a list of individual category names.

        This method takes a single string containing category names separated by
        commas, splits it into individual category names, and trims any excess
        whitespace from each category. If the input string is empty or None,
        it returns an empty list.

        Args:
            categories_string: A comma-separated string of category names.

        Returns:
            A list of category names as strings. If the input string is empty
            or None, the returned list will be empty.
        """
        if categories_string:
            return [category.strip() for category in categories_string.split(',')]
        return []
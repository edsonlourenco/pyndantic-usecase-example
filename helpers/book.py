import pathlib


class BookHelper:
    """
    Handles operations related to book data and provides utility functions.

    The BookHelper class contains static methods that assist in managing
    and retrieving book resources, such as paths to datasource files. It
    is designed to be used in scenarios where book metadata is stored and
    accessed from specific file locations. The class encapsulates the details
    of file system paths to simplify access to resources.

    Attributes:
        None
    """

    @staticmethod
    def get_json_path() -> str:
        """
        Returns the file path to the JSON resource containing book data.

        The method generates a path to the `books_fake.json` file, which is located
        in a specific directory relative to the caller's file system location. It
        ensures the appropriate relative path structure to reach the JSON file,
        intended to be used as a datasource.

        @return: Absolute file path to the target JSON file as a string.
        """
        # Adjust the path to point to the desired relative location
        return pathlib.Path(__file__).parent.parent / 'datasources' / 'json' / 'books_fake.json'
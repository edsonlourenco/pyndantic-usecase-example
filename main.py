"""
Main module for running the book data processing application.
"""

from usecases.book_usecase import BookUseCase


def main(book_usecase: BookUseCase):
    """
    Main function to read books data from JSON format using a BookUseCase
    object and print their representations. This function utilizes the BookUseCase
    class methods to handle the data fetching and processing.

    Arguments:
        book_usecase (BookUseCase): The use case object responsible for reading and
            managing book-related data.
    """
    top_5_json_books = book_usecase.read_from_json(5)

    print(repr(top_5_json_books))


if __name__ == "__main__":
    book_usecase = BookUseCase()
    main(book_usecase)

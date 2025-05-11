from pydantic import BaseModel


class Book(BaseModel):
    """
    Represents a book entity with attributes associated to its details.

    This class is used to model the properties and characteristics of a book,
    including its identification, categorization, and description. It serves as
    a base to define individual book entries with all necessary metadata
    attributes relevant to handling and processing book information.
    """

    _id: int
    title: str
    isbn: str
    pageCount: int
    publishedDate: str
    thumbnailUrl: str
    shortDescription: str
    longDescription: str
    status: str
    authors: list[str]
    categories: list[str]
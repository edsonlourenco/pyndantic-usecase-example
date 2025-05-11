import json
import random
from faker import Faker

# Initialize Faker for generating fake data
fake = Faker()

def generate_book(id):
    """
    Generate a mock book entry with various attributes.

    This function creates a dictionary representing a book
    with random values for attributes such as title, ISBN, page count,
    publication date, and additional descriptors. It utilizes randomization
    and faker library to populate fields dynamically.

    Arguments:
        id (Any): The identifier for the book.

    Returns:
        dict: A dictionary containing the generated book details.
    """
    return {
        "_id": id,
        "title": fake.sentence(nb_words=4),
        "isbn": fake.isbn13(),
        "pageCount": random.randint(50, 1000),
        "publishedDate": fake.date_between(start_date='-30y', end_date='today').isoformat(),
        "thumbnailUrl": fake.image_url(width=200, height=300),
        "shortDescription": fake.text(max_nb_chars=200),
        "longDescription": fake.text(max_nb_chars=1000),
        "status": random.choice(["PUBLISH", "DRAFT", "REVIEW"]),
        "authors": [fake.name() for _ in range(random.randint(1, 3))],
        "categories": [fake.word() for _ in range(random.randint(1, 3))]
    }

# Function to export the list of books to a JSON file
def exports_json(books, filename='json/books_fake.json'):
    """
    Exports a list of books to a JSON file with specified formatting.

    This function writes a list of book data to a JSON file, ensuring that the
    data is properly formatted with a specified indentation and UTF-8 encoding.
    After the export is completed, a message is printed indicating the file's
    save location.

    Arguments:
        books (list): A list containing book data to be exported to the JSON file.
        filename (str): Optional. The path and name of the JSON file where the
            data will be saved. Defaults to 'json/books_fake.json'.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
    print(f"JSON file saved as {filename}")

# Generate 1000 fake books
books = [generate_book(i) for i in range(1, 1001)]

# Export the data to JSON
exports_json(books)
# 📚 Fake Books Dataset Generator

A simple yet powerful Python-based project to generate synthetic datasets of fake books using `Faker` and `Pydantic`. This project is perfect for testing, learning, or building prototypes involving structured book data. Built with love by [Edson Lourenço](mailto:edson.lourenco.dev@gmail.com) 💙

> ⚙️ Data Engineer | 🧠 Software Engineer | 🖥️ Infrastructure background

---

## ✨ Features

- ✅ Generate realistic fake book data with `faker`
- ✅ Validate data schemas using `pydantic`
- ✅ Export data to JSON format
- ✅ Organized code with helpers, use cases, and schema validation
- ✅ Unit tested with a clean architecture
- ✅ Modular and extensible design

---

## 🗂️ Project Structure

```bash
.
├── LICENSE
├── README.md
├── __init__.py
├── datasources
│   ├── faker_dataset_generator.py        # Generates the dataset
│   └── json
│       └── books_fake.json               # Example output data
├── helpers
│   └── book.py                           # Book helper functions
├── main.py                               # Entry point
├── requirements.txt
├── schemas
│   └── book.py                           # Pydantic book schema
├── tests
│   ├── helpers
│   │   └── test_book_helper.py           # Unit tests for helpers
│   └── usecases
│       └── test_dataset_json.py          # Unit tests for dataset generation
├── tree.txt
└── usecases
    └── book_usecase.py                   # Dataset generation logic
```

---

## 🧪 Requirements

Make sure to have Python 3.10+ and create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### `requirements.txt`

```text
pydantic
faker
```

---

## 🚀 How to Run

Simply run the `main.py` to generate a fake books dataset:

```bash
python main.py
```

The output JSON file will be saved at:  
📁 `datasources/json/books_fake.json`

---

## 🧠 Schema Overview

All books follow the schema defined in `schemas/book.py` using `pydantic`. This ensures each generated object is valid and consistent.

---

## ✅ Testing

Run all tests using:

```bash
python -m unittest discover -v
```

Tests are located in the `tests/` folder, split by responsibility.

---

## 🔧 Use Cases

Inside `usecases/book_usecase.py`, the logic for generating and saving datasets is centralized. It's easily extendable if you want to include more fields or change output formats (e.g., CSV, XML, etc).

---

## 📸 Sample Output

Here's a snippet of what the fake data looks like:

```json
 {
    "_id": 11,
    "title": "Arrive family newspaper.",
    "isbn": "978-1-81508-929-9",
    "pageCount": 357,
    "publishedDate": "2004-05-16",
    "thumbnailUrl": "https://picsum.photos/200/300",
    "shortDescription": "Here career suddenly sense. Firm economy everyone prove wrong.\nDevelop to agency or. Have sign our style. Congress mother others politics parent message.",
    "longDescription": "Begin early lawyer event trade meeting mean. Action color lose population information security. Commercial thus operation many voice land bit.\nAbility blood focus job two present already long. Goal local dream could likely month. Pull management democratic him science watch. Perform bank establish rich.\nPiece risk voice film prove. Price former ever guess art about.\nSoon magazine daughter. Though final drug economy lead.\nHave concern produce data relate hold fill. Agree question program record.\nSimply Mr down new them. Young defense real raise open.\nCase action position later. Follow including magazine Mrs. Degree break home cover receive policy.\nPage indicate usually herself chance world business. West study movement his. Laugh public smile station away exist management second.\nRecord remain blue newspaper this put. Find about something how perhaps surface. Food east involve.\nPresent after task blue. During manage many firm impact hope. Issue force a several.",
    "status": "REVIEW",
    "authors": [
      "Isaiah Cooper",
      "Amber Dominguez"
    ],
    "categories": [
      "improve",
      "offer"
    ]
  }
```

The full dataset is in [`books_fake.json`](./datasources/json/books_fake.json)

---

## 🤝 Contributing

Pull requests are welcome! If you want to improve or extend the project, feel free to fork and open a PR.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## 🙋 About the Author

**Edson Lourenço**  
👨🏾‍💻 Data Engineer with roots in infrastructure and software engineering  
📧 [edson.lourenco.dev@gmail.com](mailto:edson.lourenco.dev@gmail.com)  
💼 Passionate about data, automation, and clean code

---

## 🌟 Show your support

If you liked this project, give it a ⭐ on GitHub and share it with your network!

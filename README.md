# Gutenberg Books API

A RESTful API built using **Django**, **Django REST Framework**, and **PostgreSQL** to query and access books data from **Project Gutenberg**.  
The API supports filtering, pagination, and ordering by popularity.

---

##  System Overview


- Backend **REST API** built using **Django** and **Django REST Framework**
- Provides structured access to **Project Gutenberg book metadata**
- Uses **PostgreSQL** database imported from an existing data dump
- Exposes a **single public endpoint** to fetch books and related data
- Returns books along with:
  - Authors
  - Subjects
  - Bookshelves
  - Languages
  - Download formats
- Supports **flexible filtering** using multiple query parameters
- Allows **partial and case-insensitive matching**
- Supports **multiple values per filter** via comma-separated inputs
- Topic-based search works across **subjects and bookshelves**
- Filtering is handled at the **database level using Django ORM**
- Results are **paginated** with a fixed page size of **25 records**
- Books are **ordered by download count (popularity)** in descending order
- Designed to work with an **existing database schema**
- Uses **unmanaged Django models** to map pre-existing tables
- Ensures **data integrity**, clean API design, and scalable performance

---

## Tech Stack

- **Backend**: Python, Django, Django REST Framework  
- **Database**: PostgreSQL  
- **ORM**: Django ORM (with unmanaged models)  
- **Version Control**: Git & GitHub  
- **Environment Management**: python-dotenv  

---

##  Project Structure

```text
gutenberg-books-api/
├── backend/
│   ├── books/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── pagination.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── books_api/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── manage.py
|   └── .env
|
├── requirements.txt
├── README.md
└── .gitignore

```

---

## Database Design

The database schema is imported from a PostgreSQL dump and includes:

- `books_book` – core book information
- `books_author` – author details
- `books_subject` – subject tags
- `books_bookshelf` – bookshelf categories
- `books_language` – language codes
- Junction tables for many-to-many relationships
- `books_format` – download links by mime-type

 **Important**  
All Django models use `managed = False` since tables already exist in the database.

---

##  API Endpoint

### Base URL

/api/books/


---

##  API Response Format

```json
{
  "count": 34000,
  "next": "/api/books/?page=2",
  "previous": null,
  "results": [
    {
      "gutenberg_id": 1342,
      "title": "Pride and Prejudice",
      "authors": [
        {
          "name": "Austen, Jane",
          "birth_year": 1775,
          "death_year": 1817
        }
      ],
      "subjects": ["Courtship -- Fiction"],
      "bookshelves": ["Best Books Ever Listings"],
      "languages": ["en"],
      "formats": {
        "application/pdf": "https://www.gutenberg.org/files/1342/1342-pdf.pdf"
      },
      "download_count": 44776
    }
  ]
}
```

---

## Supported Filters

All filters are **optional**, **case-insensitive**, and **can be combined** in a single API call.  
Multiple values per filter are supported using comma-separated values.

###  Gutenberg ID (multiple values supported)

?gutenberg_id=1342  
?gutenberg_id=11,74,1342

---

### Title (partial match, case-insensitive, multiple values supported)

?title=pride  
?title=pride,adventure

---

### Author (partial match,case-insensitive, multiple values supported)

?author=austen  
?author=austen,mark

---

### Language (multiple values supported)

?language=en  
?language=en,fr

---

### Topic (Subject OR Bookshelf, partial match, case-insensitive, multiple values supported)

?topic=child  
?topic=child,children

---

### Mime-type (multiple values supported)
?mime-type=pdf  
?mime-type=pdf,text

### Combined Filters

/api/books/?language=en&topic=child,children&author=carroll

---

## Pagination

- Fixed page size: **25 books per request**
- Page-number based pagination


### Examples

/api/books/  
?page=2  
?page=10

---
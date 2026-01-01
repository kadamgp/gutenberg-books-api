# Gutenberg Books API

A RESTful API built using **Django**, **Django REST Framework**, and **PostgreSQL** to query and access books data from **Project Gutenberg**.  
The API supports filtering, pagination, and ordering by popularity.

**Live API:**  
https://gutenberg-books-api.onrender.com/api/books/



##  API Endpoint


### List Books
**GET** `/api/books/`

**Live URL:**  
https://gutenberg-books-api.onrender.com/api/books/

---

### Example Requests

Filter by language:
https://gutenberg-books-api.onrender.com/api/books/?language=en

Filter by multiple IDs:
https://gutenberg-books-api.onrender.com/api/books/?gutenberg_id=456,2

---

## Supported Filters

All filters are **optional**, **case-insensitive**, and **can be combined** in a single API call.  
Multiple values per filter are supported using comma-separated values.

-  Gutenberg ID (multiple values supported)

/api/books/?gutenberg_id=1342  
/api/books/?gutenberg_id=11,74,1342

---

- Title (partial match, case-insensitive, multiple values supported)

api/books/?title=pride  
api/books/?title=pride,adventure

---

- Author (partial match,case-insensitive, multiple values supported)

api/books/?author=austen  
api/books/?author=austen,mark

---

- Language (multiple values supported)

api/books/?language=en  
api/books/?language=en,fr

---

- Topic (Subject OR Bookshelf, partial match, case-insensitive, multiple values supported)

api/books/?topic=child  
api/books/?topic=child,children

---

- Mime-type (multiple values supported)

api/books/?mime-type=pdf  
api/books/?mime-type=pdf,text

---
- Combined Filters

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
│   ├── books/   ( app )
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── pagination.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── books_api/  ( main project)
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── manage.py
|   ├── requirements.txt
|   └── .env
|
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


## Step-by-Step Approach to Build the Project

This section outlines the exact process followed to design, build, and deploy the Gutenberg Books API.

### Step 1: Database Understanding
- Analyzed PostgreSQL version of `gutendex.dump`
- Identified core tables and relationships
- Mapped database fields to API requirements

### Step 2: Tools and Technology Selection
- Chose Python, Django, DRF, PostgreSQL
- Selected tools based on scalability and assessment requirements

### Step 3: Django Project Setup
- Initialized Git repository
- Created virtual environment
- Installed required dependencies
- Created Django project and books app

### Step 4: Environment Configuration
- Configured `.env` for secrets and database access
- Set up environment-based settings for local and production

### Step 5: Mapping Existing Database to Django Models
- Created unmanaged Django models (`managed = False`)
- Defined relationships and junction tables
- Matched Django models to existing PostgreSQL schema

### Step 6: ORM Validation
- Tested queries using Django shell
- Verified joins and relationships
- Confirmed correct data retrieval

### Step 7: Version Control
- Committed stable database and model configuration
- Maintained clean Git history

### Step 8: Serializer Design
- Created serializers to shape API response
- Implemented nested serialization for related data

### Step 9: API View Implementation
- Built `/api/books/` endpoint using DRF
- Implemented queryset-based logic

### Step 10: Filtering Logic
- Implemented all filters at queryset level
- Supported multiple values per filter
- Enabled partial and case-insensitive matching
- Ensured all filters are combinable

### Step 11: Pagination
- Applied DRF pagination
- Fixed page size to 25 records per request
- Returned count, next, and previous links

### Step 12: API Testing
- Tested endpoints using browser and Postman
- Verified filter combinations and edge cases

### Step 13: Deployment Configuration
- Prepared project for production
- Configured environment variables
- Ensured database fallback for local users

### Step 14: Deployment on Render
- Connected GitHub repository to Render
- Set build and start commands
- Deployed API with PostgreSQL backend
- Verified public accessibility

---

## Author
 
**Gangaprasad Kadam**  
MCA (Computer Science), Pune University  
GitHub: https://github.com/kadamgp/gutenberg-books-api  
LinkedIn: https://linkedin.com/in/kadamgp

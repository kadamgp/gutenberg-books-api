from django.db import models

# Create your models here.


# ------------------- Lookup Models -------------------

# Author Model


class Author(models.Model):
    name = models.CharField(max_length=128)
    birth_year = models.IntegerField(null=True)
    death_year = models.IntegerField(null=True)

    class Meta:
        db_table = "books_author"
        managed = False

    def __str__(self):
        return self.name

# Subject Model


class Subject(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = "books_subject"
        managed = False

    def __str__(self):
        return self.name


# Language Model
class Language(models.Model):
    code = models.CharField(max_length=4)

    class Meta:
        db_table = "books_language"
        managed = False

    def __str__(self):
        return self.code


# Bookshelf Model
class Bookshelf(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "books_bookshelf"
        managed = False

    def __str__(self):
        return self.name

# ----------------------- Junction Models -----------------------

# BookAuthor Model


class BookAuthor(models.Model):
    book = models.ForeignKey("Book", on_delete=models.DO_NOTHING)
    author = models.ForeignKey("Author", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "books_book_authors"
        managed = False

# BookSubject Model


class BookSubject(models.Model):
    book = models.ForeignKey("Book", on_delete=models.DO_NOTHING)
    subject = models.ForeignKey("Subject", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "books_book_subjects"
        managed = False


# BookLanguage Model
class BookLanguage(models.Model):
    book = models.ForeignKey("Book", on_delete=models.DO_NOTHING)
    language = models.ForeignKey("Language", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "books_book_languages"
        managed = False

# BookBookShelf Model


class BookBookshelf(models.Model):
    book = models.ForeignKey("Book", on_delete=models.DO_NOTHING)
    bookshelf = models.ForeignKey("Bookshelf", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "books_book_bookshelves"
        managed = False

# ----------------------- Main Models(Book Model) -----------------------

# Book Model


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    gutenberg_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=1024, null=True)
    download_count = models.IntegerField(null=True)
    media_type = models.CharField(max_length=16)

    # Adding Relationships to Other Models

    # Many-to-Many Relationships between Books and Authors
    authors = models.ManyToManyField(
        "Author",
        through="BookAuthor",
        related_name="books"
    )

    # Many-to-Many Relationships between Books and Subjects

    subjects = models.ManyToManyField(
        "Subject",
        through="BookSubject",
        related_name="books"
    )

    # Many-to-Many Relationships between Books and Languages

    languages = models.ManyToManyField(
        "Language",
        through="BookLanguage",
        related_name="books"
    )

    # Many-to-Many Relationships between Books and Bookshelves

    bookshelves = models.ManyToManyField(
        "Bookshelf",
        through="BookBookshelf",
        related_name="books"
    )

    class Meta:
        db_table = "books_book"
        managed = False

    def __str__(self):
        return f"Book(id={self.id}, title={self.title})"


# -------------- BookFormat Model --------------

# Bookformat Model


class BookFormat(models.Model):
    mime_type = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(
        Book,
        on_delete=models.DO_NOTHING,
        related_name="formats"
    )

    class Meta:
        db_table = "books_format"
        managed = False

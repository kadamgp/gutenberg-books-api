from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    bookshelves = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    formats = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'gutenberg_id',
            'title',
            'authors',
            'subjects',
            'bookshelves',
            'languages',
            'formats',
            'download_count',
        ]

    def get_authors(self, obj):
        return [
            {
                "name": author.name,
                "birth_year": author.birth_year,
                "death_year": author.death_year,
            }
            for author in obj.authors.all()
        ]

    def get_subjects(self, obj):
        return [subject.name for subject in obj.subjects.all()]

    def get_bookshelves(self, obj):
        return [bookshelf.name for bookshelf in obj.bookshelves.all()]

    def get_languages(self, obj):
        return [language.code for language in obj.languages.all()]

    def get_formats(self, obj):
        return {
            format.mime_type: format.url for format in obj.formats.all()
        }

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from django.db.models import F
from .pagination import BookPagination

# Create your views here.


class BookListApiView(APIView):
    """
    GET /api/books/
    Returns a paginated list of books order by popularity
    """

    def get(self, request):

        # Below querey is same as SELECT * FROM books_book ORDER BY download_count DESC NULLS LAST

        books = Book.objects.all().order_by(
            F('download_count').desc(nulls_last=True))

        paginator = BookPagination()
        paginated_books = paginator.paginate_queryset(books, request)

        serializer = BookSerializer(paginated_books, many=True)

        return paginator.get_paginated_response(serializer.data)

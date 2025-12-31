from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from django.db.models import F

# Create your views here.


class BookListApiView(APIView):
    """
    GET /api/books/
    returns a list of books order by popularity descending
    """

    def get(self, request):

        # Below querey is same as SELECT * FROM books_book ORDER BY download_count DESC NULLS LAST

        books = Book.objects.all().order_by(
            F('download_count').desc(nulls_last=True))[:5]

        serializer = BookSerializer(books, many=True)

        return Response(
            {
                "count": books.count(),
                "results": serializer.data,
            }
        )

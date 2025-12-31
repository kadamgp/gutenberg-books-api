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
    Supports filtering, ordering, and pagination
    """

    def get(self, request):

        # select * from books_book

        books = Book.objects.all()

        # Filtering
        # gutenberg_id filter
        gutenberg_ids = request.GET.getlist("gutenberg_id")

        if gutenberg_ids:
            # Convert ['1', '2', '3'] → [1, 2, 3]
            try:
                ids = [int(i) for i in gutenberg_ids]
                books = books.filter(gutenberg_id__in=ids)
            except ValueError:
                return Response(
                    {"error": "gutenberg_id must be integers"},
                    status=400
                )
                # Remove duplicated books due to joins
        queryset = books.distinct()

        # Order by Popularity
        queryset = queryset.order_by(
            F('download_count').desc(nulls_last=True)
        )
        # Pagination
        paginator = BookPagination()
        paginated_books = paginator.paginate_queryset(queryset, request)

        serializer = BookSerializer(paginated_books, many=True)

        return paginator.get_paginated_response(serializer.data)

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from django.db.models import F, Q
from .pagination import BookPagination

# Create your views here.


class BookListApiView(APIView):
    """
    GET /api/books/
    Supports filtering, ordering, and pagination
    """

    def get(self, request):

        # select * from books_book

        queryset = Book.objects.all()

        # Filtering
        # 1. gutenberg_id filter (/?gutenberg_id=1&gutenberg_id=2)

        gutenberg_ids = request.GET.get("gutenberg_id")

        if gutenberg_ids:
            # Convert "1,2,3" - > ['1', '2', '3'] -> [1, 2, 3]
            try:
                ids = [int(i.strip()) for i in gutenberg_ids.split(",")]
                queryset = queryset.filter(gutenberg_id__in=ids)
            except ValueError:
                return Response(
                    {"error": "gutenberg_id must be a comma-separated list of integers"},
                    status=400
                )

        # 2. title filter (partial, case-insensitive)

        title_param = request.GET.get("title")
        if title_param:
            titles = [title.strip()
                      for title in title_param.split(",") if title.strip()]

            title_query = Q()
            for title in titles:
                title_query |= Q(title__icontains=title)

            queryset = queryset.filter(title_query)

        # 3. author filter (partial, case-insensitive)

        author_param = request.GET.get("author")
        if author_param:
            authors = [author.strip()
                       for author in author_param.split(",") if author.strip()]

            author_query = Q()
            for author in authors:
                author_query |= Q(authors__name__icontains=author)

            queryset = queryset.filter(author_query)

        # 4. language filter (multiple values)

        language_param = request.GET.get("language")
        if language_param:
            lang_codes = [lang.strip()
                          for lang in language_param.split(",") if lang.strip()]

            lang_query = Q()
            for l in lang_codes:
                lang_query |= Q(languages__code__icontains=l)

            queryset = queryset.filter(lang_query)

        # 5.topic filter (subject or bookshelf)
        topic_param = request.GET.get("topic")
        if topic_param:
            topics = [t.strip() for t in topic_param.split(",") if t.strip()]

            topic_query = Q()
            for t in topics:
                topic_query |= Q(subjects__name__icontains=t)
                topic_query |= Q(bookshelves__name__icontains=t)

            queryset = queryset.filter(topic_query)

        # 6. mime-type filter

        mime_param = request.GET.get("mime-type")
        if mime_param:
            mime_types = [mime.strip()
                          for mime in mime_param.split(",") if mime.strip()]

            mime_query = Q()
            for mime_type in mime_types:
                mime_query |= Q(formats__mime_type__icontains=mime_type)

            queryset = queryset.filter(mime_query)

        # Remove duplicated books due to joins
        queryset = queryset.distinct()

        # Order by Popularity
        queryset = queryset.order_by(
            F('download_count').desc(nulls_last=True)
        )
        # Pagination
        paginator = BookPagination()
        paginated_books = paginator.paginate_queryset(queryset, request)

        serializer = BookSerializer(paginated_books, many=True)

        return paginator.get_paginated_response(serializer.data)

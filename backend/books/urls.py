from django.urls import path
from .views import BookListApiView

urlpatterns = [
    path('books/', BookListApiView.as_view(), name='book-list'),
]

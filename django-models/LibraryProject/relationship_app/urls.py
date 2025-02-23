from django.urls import path
from .views import LibraryDetailView, list_books
urlpatterns = [
    path("books/", list_books, name='list_books'),
    path("library/<int:id>", LibraryDetailView.as_view(), name='library')
]

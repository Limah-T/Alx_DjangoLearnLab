from django.urls import path
from relationship_app import views
urlpatterns = [
    path("books/", views.list_books, name='list_books'),
    path("library/<int:id>", views.ListBookView.as_view(), name='library')
]

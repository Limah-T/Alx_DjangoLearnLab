from django.urls import path
from .views import LibraryDetailView, SignUpView
from .views import list_books
from django.contrib.auth import views

urlpatterns = [
    path("books/", list_books, name='list_books'),
    path("library/<int:pk>", LibraryDetailView.as_view(), name='library'),
    path("register/", SignUpView.as_view(), name='register'),
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name="logout")
]

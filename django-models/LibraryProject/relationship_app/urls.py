from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth import views
from . import views
# SignUpView, register
urlpatterns = [
    path("books/", list_books, name='list_books'),
    path("library/<int:pk>", LibraryDetailView.as_view(), name='library'),
    path("register/", views.register, name='register'),
    path("login/", views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    # path("logout/", views.LogoutView.as_view(template_name='relationship_app/logout.html') ,name="logout")
]

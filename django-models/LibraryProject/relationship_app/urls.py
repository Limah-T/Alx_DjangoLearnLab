from django.urls import path
from .views import LibraryDetailView
from .views import list_books, is_admin, is_member, is_librarian
from django.contrib.auth import views
from . import views

# SignUpView, register

urlpatterns = [
    path("books/", list_books, name='list_books'),
    path("library/<int:pk>", LibraryDetailView.as_view(), name='library'),
    path("register/", views.register, name='register'),
    path("login/", views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", views.LogoutView.as_view(template_name='relationship_app/logout.html') ,name="logout"),
    path('admin-view/', is_admin, name='admin_view'),
    path("member_view/", is_member, name="member_view"),
    path("librarian_view/", is_librarian, name="librarian_view")
]

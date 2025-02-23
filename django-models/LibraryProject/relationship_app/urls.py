from django.urls import path
from .views import LibraryDetailView, SignUpView, register
from .views import list_books, admin_view, member_view, librarian_view
from django.contrib.auth import views
from . import views

urlpatterns = [
    path("books/", list_books, name='list_books'),
    path("library/<int:pk>", LibraryDetailView.as_view(), name='library'),
    path("register/", views.register, name='register'),
    path("login/", views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", views.LogoutView.as_view(template_name='relationship_app/logout.html') ,name="logout"),
    path("admin_view/<int:pk>", admin_view, name="admin"),
    path("member_view/<int:pk>", member_view, name="member"),
    path("librarian_view/<int:pk>", librarian_view, name="librarian_view")
]

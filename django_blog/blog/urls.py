from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('profile/<int:id>/', views.ProfileView.as_view(), name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('logout/', views.logoutview, name='logout'),
    path('user/<int:id>/', views.UserPageView.as_view(), name='userposts'),
    path('posts/new/', views.createpostview, name='create-post'),
    path('posts/<int:pk>/edit/', views.edit_post, name='update-post'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete-post'),
]
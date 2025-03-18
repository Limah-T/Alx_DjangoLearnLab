from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerview, name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('home', views.homepageview, name='home'),
    path('profile/', views.profileview, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('logout/', views.logoutview, name='logout'),
]
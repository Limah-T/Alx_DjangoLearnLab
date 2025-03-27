from django.urls import path
from .import views
from django.contrib.auth import views as authviews

urlpatterns = [
    # path('register', views.RegistrationView.as_view(), name='register'),
    # path('home', views.HomePage.as_view(), name='home'),
    # path('login', authviews.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # API URLS
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
]
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import RegistrationForm
from .models import CustomUser
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status

# Create your views here.
class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            # print(form.cleaned_data.get('username'))
            # print(form.cleaned_data.get('password1'))
            # print(form.cleaned_data.get('password2'))
            form.save()
        return super().form_valid(form)
    
class HomePage(generic.ListView):
    model = CustomUser
    template_name = 'accounts/home.html'
    context_object_name = 'all_users'

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

"""Views for Serializers"""
class RegisterAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            serializer.validated_data.pop('password1')
            password = serializer.validated_data.pop('password2')
            user = CustomUser(username=username)
            user.set_password(password)
            user.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)       
        return super().create(request, *args, **kwargs)
    

class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializers = LoginSerializer(data=request.data)
        if serializers.is_valid():
            print('inside')
            username = serializers.validated_data.get('username')
            password = serializers.validated_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                token = Token.objects.get(user=user)
                login(request, user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            print('outside')
            return Response({'error': 'username or password is incorrect!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


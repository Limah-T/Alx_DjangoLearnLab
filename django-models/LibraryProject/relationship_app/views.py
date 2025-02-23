from django.shortcuts import render, redirect
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", context={'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class LoginView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/login.html'

@login_required
def profile_view(request):
    # This view can only be accessed by authenticated users
    return render(request, 'profile.html')

        


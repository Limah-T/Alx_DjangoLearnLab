from django.shortcuts import render, redirect
from .models import Library
from .models import Book
from .models import UserProfile
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login


# Create your views here
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", context={'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name='relationship_app/register.html', name='register')
    else:
        form = UserCreationForm()
        return render(request, template_name='relationship_app/register.html')

class LoginView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy(login)
    template_name = 'relationship_app/login.html'

@login_required
def profile_view(request):
    # This view can only be accessed by authenticated users
    return render(request, 'profile.html')

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == "Member"

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# def is_admin(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'admin_page.html')

# def is_librarian(user):
#     return user.userprofile.role == "Librarian"

# def is_member(user):
#     return user.userprofile.role == "Member"



# @login_required
# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'librarian_view')

# @login_required
# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'member_view')




from django.shortcuts import render, redirect
from .models import Library
from .models import Book
from .models import UserProfile
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

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

        
def admin_view(request, user_id):
    user = get_object_or_404(UserProfile, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm("relationship_app.admin_view")
    content_type = ContentType.objects.get_for_model(UserProfile)
    permission = Permission.objects.get(
        codename="change_blogpost",
        content_type=content_type,
    )
    user.user_permissions.add(permission)

def librarian_view(request, user_id):
    # Checking the cached permission set
    user = get_object_or_404(User, pk=user_id)
    user.has_perm("relationship_app.librarian_view")  # False
    content_type = ContentType.objects.get_for_model(UserProfile)
    permission = Permission.objects.get(
        codename="change_blogpost",
        content_type=content_type,
    )

    user.user_permissions.add(permission)

def member_view(request, user_id):
    # Checking the cached permission set
    user = get_object_or_404(User, pk=user_id)
    user.has_perm("relationship_app.member_view")  # False
    content_type = ContentType.objects.get_for_model(UserProfile)
    permission = Permission.objects.get(
        codename="change_blogpost",
        content_type=content_type,
    )

    user.user_permissions.add(permission)



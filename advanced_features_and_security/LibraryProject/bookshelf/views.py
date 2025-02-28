from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
# Create your views here.

# @permission_required('bookshelf.can_create_book', raise_exception=True)
def create_view(request):
    if request.user.has_perm('bookshelf.can_create_book'):
        all_books = [
            {'id': 1, 'title': 'Python', 'author': 'Guido Van Rossum'},
            {'id': 2, 'title': 'Django', 'author': 'Guido Van Rossum'},
            {'id': 3, 'title': 'Flask', 'author': 'Guido Van Rossum'}
        ]
        return render(request, 'bookshelf/create.html', {'all_books': all_books})
    else:
        return HttpResponse("You are not permitted to create book!")

@permission_required('bookshelf.can_view', raise_exception=True)
def edit_view(request):
    
    return render(request, 'bookshelf/view.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/edit.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/delete.html')


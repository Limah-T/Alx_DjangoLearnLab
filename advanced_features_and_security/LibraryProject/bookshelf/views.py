from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
# Create your views here.

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    all_books = [
        {'id': 1, 'title': 'Python', 'author': 'Guido Van Rossum'},
        {'id': 2, 'title': 'Django', 'author': 'Guido Van Rossum'},
        {'id': 3, 'title': 'Flask', 'author': 'Guido Van Rossum'}
    ]
    return render(request, 'bookshelf/view.html', {'all_books': all_books})

@permission_required('bookshelf.can_create_book', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/create.html')

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/edit.html')

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/delete.html')


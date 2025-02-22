from .models import Book, Author, Library, Librarian

author = Author.objects.create(name="Limah")
author.save()
author_name = Author.objects.filter(author=author)
book = Book.objects.create(title="Python", author=author_name)
book.save()
book = Book.objects.create(title="Flask", author=author_name)
book.save()
library_name = Library.objects.create(name = "HardCopySections", book = book)
library_name.save()
librarian_name = Librarian(name = "Palmer")
librarian_name.save()

# Query all books by a specific author.
book = Book.objects.filter(author=1)
print(book.values())

# List all books in a library.
books = Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library.
librarian = Librarian.objects.filter(library=librarian_name)
print(librarian_name)


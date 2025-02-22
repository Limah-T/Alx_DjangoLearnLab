from .models import Book, Author, Library, Librarian

author = Author.objects.create(name="Limah")
author.save()
book = Book.objects.create(title="Python", author=author)
book.save()
book = Book.objects.create(title="Flask", author=author)
book.save()
library = Library.objects.create(name = "HardCopySections", book = book)
library.save()
librarian = Librarian(name = "Palmer")
librarian.save()

# Query all books by a specific author.
book = Book.objects.filter(author=1)
print(book.values())

# List all books in a library.
books = Library.objects.get(name=library)
books.all()

# Retrieve the librarian for a library.
librarian = Librarian.objects.filter(library=librarian)
print(librarian)


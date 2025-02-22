from .models import Book, Author, Library, Librarian

# Query all books by a specific author.
author = Author.objects.create(name="Limah")
author.save()
book = Book.objects.create(title="Python", author=author)
book.save()
book = Book.objects.create(title="Flask", author=author)
book.save()
book = Book.objects.filter(author=1)
print(book.values())

# List all books in a library.
books = Book.objects.all()
print(books)

# Retrieve the librarian for a library.
library = Library.objects.create(name = "HardCopySections")
library.save()

librarian = Librarian(name = "Palmer")
librarian.save()




from .models import Book, Author

# Query all books by a specific author.
author = Author.objects.create(name="Limah")
author.save()
book = Book.objects.create(title="Python", author=author)
book.save()
book = Book.objects.create(title="Flask", author=author)
book.save()
book = Book.objects.filter(author=1)
print(book.values())
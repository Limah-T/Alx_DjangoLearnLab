Retrieve and display all attributes of the book you just created.

book = Book.objects.values()
print(book)

<!-- <QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}] -->
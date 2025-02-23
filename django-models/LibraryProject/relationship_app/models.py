from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication_year = models.DateField(default="2020-03-15")

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="library")

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return f"User: {self.name}, {self.email}"
    
class UserProfile(models.Model):
    choices = {
        'ADMIN': 'Admin',
        'LIBRARIAN': 'Libarian',
        'MEMBER': 'Member'
    }
    role = models.CharField(max_length=100, choices=choices, default=choices['MEMBER'])
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    def __str__(self):
        return f"UserProfile: {self.role} to {UserProfile.user.username}"
    
    


    
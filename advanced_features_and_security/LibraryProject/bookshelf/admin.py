from django.contrib import admin
from .models import CustomUser, Book

# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo')

class BookAdmin(admin.ModelAdmin):
    list_filter = (("title", "author"))
    search_fields = ("title", "author")

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomModelAdmin)
# user = CustomUser.objects.create_user(username="Root", email="root@gmail.com",password="123root098", date_of_birth="1990-1-1")
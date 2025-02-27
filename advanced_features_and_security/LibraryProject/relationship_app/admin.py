from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo')

admin.site.register(CustomUser, CustomModelAdmin)
# user = CustomUser.objects.create_user(username="Root", email="root@gmail.com",password="123root098", date_of_birth="1990-1-1")

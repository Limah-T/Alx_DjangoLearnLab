from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


# Perform generic views operation on Book Model
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Perform viewsets Operation on Book Model
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



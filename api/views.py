from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
import requests

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def books_page(request):
    # URL локального API
    response = requests.get("http://127.0.0.1:8000/api/books/")
    books = response.json()
    return render(request, "books_page.html", {"books": books})
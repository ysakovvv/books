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
    # Бардык китептерди DBдан алабыз
    books = Book.objects.all()

    # Templateке жөнөтөбүз
    return render(request, 'books_page.html', {'books': books})

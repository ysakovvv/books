from api import admin
from django.urls import path
from .views import BookList,BookCreate,books_page

urlpatterns = [
    path('api/books/', BookList.as_view(),name='book-list'),
    path('api/books/create', BookCreate.as_view(), name='book_create'),
    path('', books_page, name='home'),
]



from django.urls import path
from .import views
from views import lists_all_books
from views import LibraryDetailView

urlpatterns = [
    path('books/', lists_all_books.as_view(), name= 'books'),
    path('library/', LibraryDetailView.as_view(), name='library-details'),
]

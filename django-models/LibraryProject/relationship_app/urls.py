from django.urls import path
from .import views
from views import LibraryDetailView

urlpatterns = [
    path('books/', views.lists_all_books, name= 'books'),
    path('library/', LibraryDetailView.as_view(), name='library-details'),
]

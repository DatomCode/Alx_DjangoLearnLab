from django.urls import path, include
from .views import SignUp
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name= 'books'),
    path('library/', LibraryDetailView.as_view(), name='library-details'),
    path('', include()),
    path('register/', SignUp, name ="register")
]

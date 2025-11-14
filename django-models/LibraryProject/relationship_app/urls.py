from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
    path('books/', list_books, name= 'books'),
    path('library/', LibraryDetailView.as_view(), name='library-details'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin_area/', views.admin_view, name='admin_view'),
    path('librarian_area/', views.librarian_view, name='librarian_view'),
    path('member_area/', views.member_view, name='member_view'),
    path('books/add/', views.secured_book_add, name='book_add'),
    path('books/edit/<int:pk>/', views.secured_book_edit, name='book_edit'),
    path('books/delete/<int:pk>/', views.secured_book_delete, name='book_delete'),
]



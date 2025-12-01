from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import  IsAuthenticated
from django_filters import rest_framework
from rest_framework import filters

# ListView: Retrieve all books


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [
        rest_framework.DjangoFilterBackend, # Enables field-based filtering (e.g., ?publication_year=2020)
        filters.SearchFilter,               # Enables text search (e.g., ?search=Chinua)
        filters.OrderingFilter              # Enables sorting (e.g., ?ordering=publication_year)
    ]

    # 1. Configuration for DjangoFilterBackend
    filterset_fields = ['title', 'author', 'publication_year']

    # 2. Configuration for SearchFilter
    search_fields = ['title', 'author__name']

    # 3. Configuration for OrderingFilter
    ordering_fields = ['title', 'publication_year']

    # Set a default ordering
    ordering = ['title']


# DetailView: Retrieve a single book by ID

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CreateView: Add a new book

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can create

    def perform_create(self, serializer):
        serializer.save()

# UpdateView: Modify an existing book

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can edit

    def perform_update(self, serializer):
        serializer.save()

# DeleteView: Remove a book

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can delete

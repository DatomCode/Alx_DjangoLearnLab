from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library


# Create your views here.

def lists_all_books(request):
    books = Book.objects.all()
    return render(request, 'books/lists_book.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "books/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all()
        return context
        
    
        

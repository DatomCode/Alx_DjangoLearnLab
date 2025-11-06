from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book
from .models import Library




# Create your views here.

def lists_all_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all()
        return context
        
    
        

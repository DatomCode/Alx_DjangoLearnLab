from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book 
from .forms import BookForm 
from .forms import ExampleForm
# --- List View ---

# Mandatory requirement: Use raise_exception=True to return 403 Forbidden on failure
@permission_required('bookshelf.can_view', raise_exception=True) 
def book_list(request):
    """
    Displays a list of all books. Requires the 'can_view' permission.
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'bookshelf/book_list.html', context)

# --- Create View ---

# Mandatory requirement: Use raise_exception=True to return 403 Forbidden on failure
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    Handles the creation of a new book. Requires the 'can_create' permission.
    """
    if request.method == 'POST':
        # Ensure you handle form data here
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            # Assuming CustomUser has been implemented in Task 0
            book.added_by = request.user 
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
        
    context = {'form': form, 'page_title': 'Add New Book'}
    return render(request, 'bookshelf/form_example.html', context)
    
# Example of an Edit View enforcement
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    # Implementation for editing a book
    pass
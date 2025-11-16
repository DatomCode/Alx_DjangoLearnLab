from django.shortcuts import render

# Create your views here.
def book_list(request):
    """
    Displays a list of all books. Requires the 'can_view' permission.
    """
    # Task 1, Step 3 Requirement: The context variable 'books'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'bookshelf/book_list.html', context)
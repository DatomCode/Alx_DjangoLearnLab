from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Author, Book, Library, Librarian, UserProfile
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book 
from .forms import BookForm

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all()
        return context
    

# Register View

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('list-books')  # redirect to your existing page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return render(request, 'relationship_app/logout.html')



        
    


# from django.contrib import messages
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role in ['Librarian', 'Admin'] # Admin can also be librarian

def is_member(user):
    return user.is_authenticated and user.userprofile.role in ['Member', 'Librarian', 'Admin']


@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    """View accessible only to Admin users."""
    context = {'message': 'Welcome, Admin!'}
    return render(request, 'relationship_app/admin_view.html', context)

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    """View accessible only to Librarian and Admin users."""
    context = {'message': 'Welcome, Librarian!'}
    return render(request, 'relationship_app/librarian_view.html', context)

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    """View accessible to all authenticated users (Member, Librarian, Admin)."""
    context = {'message': 'Welcome, Member!'}
    return render(request, 'relationship_app/member_view.html', context)



def book_add(request):
    """Placeholder view for adding a book."""
    # In a real app, this would handle form submission
    return render(request, 'relationship_app/book_form.html', {'action': 'Add'})

def book_edit(request, pk):
    """Placeholder view for editing a book."""
    book = get_object_or_404(Book, pk=pk)
    # In a real app, this would handle form submission
    return render(request, 'relationship_app/book_form.html', {'action': 'Edit', 'book': book})

def book_delete(request, pk):
    """Placeholder view for deleting a book."""
    book = get_object_or_404(Book, pk=pk)
    # In a real app, this would handle POST request and deletion
    if request.method == 'POST':
        book.delete()
        return redirect('list_books') # Redirect to book list
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})



@permission_required('relationship_app.can_add_book', raise_exception=True)
def secured_book_add(request):
    """Secured view for adding a book."""
    # Logic for book addition goes here
    # Example: if request.method == 'POST': form = BookForm(request.POST)...
    return book_add(request)

@permission_required('relationship_app.can_change_book', raise_exception=True)
def secured_book_edit(request, pk):
    """Secured view for editing a book."""
    # Logic for book editing goes here
    return book_edit(request, pk)

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def secured_book_delete(request, pk):
    """Secured view for deleting a book."""
    # Logic for book deletion goes here
    return book_delete(request, pk)
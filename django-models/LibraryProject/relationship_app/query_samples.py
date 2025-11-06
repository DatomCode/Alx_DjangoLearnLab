from relationship_app.models import Book, Author, Library, Librarian

# 1. List all books in a library
def list_books_in_library():
    library = Library.objects.all()
    books = Book.objects.filter()
    return books

# 2. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.all()
    books = Book.objects.filter()
    return books

# 3. Retrieve the librarian for a library
def get_librarian_for_library():
    library = Library.objects.all()
    librarian = Librarian.objects.all()
    return librarian

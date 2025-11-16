from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Form based on the Book model for creation and editing.
    """
    class Meta:
        model = Book
        # Include all fields that the user should be allowed to set via the form.
        # We exclude 'added_by' since that is set automatically in the view (book_create).
        fields = ['title', 'author', 'published_date'] 
        
        # Optional: Add widgets for better UX, e.g., a DateInput for the date field
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
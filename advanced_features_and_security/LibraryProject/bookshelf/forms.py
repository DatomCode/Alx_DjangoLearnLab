from django import forms
from .models import Book

# --- ModelForm for Book (Existing) ---
class BookForm(forms.ModelForm):
    """
    Form based on the Book model for creation and editing.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date'] 
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

# --- Generic Form (New Requirement) ---
class ExampleForm(forms.Form):
    """
    A simple, non-model form used for demonstration purposes.
    """
    your_name = forms.CharField(label='Your Name', max_length=100)
    comment = forms.CharField(widget=forms.Textarea)
    is_public = forms.BooleanField(required=False, label='Share Publicly')
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

#Adding The "email" field to the built-in form we are us

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#Updating the form so the Users can see it
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class meta():
        models = User
        fields = ["username", "email"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
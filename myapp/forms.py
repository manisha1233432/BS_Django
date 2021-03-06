from django.forms import ModelForm
from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class BookForm(ModelForm):
    class Meta:
    
        model = Book
        fields = ['book','author','book_image','book_upload']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

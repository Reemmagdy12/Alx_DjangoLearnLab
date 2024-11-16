from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    age = forms.IntegerField(label='Age', min_value=0)
    message = forms.CharField(label='Message', widget=forms.Textarea)
from django.shortcuts import render
from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books' : books}
    return render (request, 'relationship_app/list_books.html', context)

from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Library
class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library
    context_object_name = 'library'



from relationship_app.models import Author, Book, Library, Librarian
Book.objects.filter(author__name="George Orwell")
Book.objects.filter(library__name= "library")
Librarian.objects.get(library__name="library")


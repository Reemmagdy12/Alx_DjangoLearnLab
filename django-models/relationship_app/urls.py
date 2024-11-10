from django.urls import path
from .views import list_books, LibraryDetail
urlpatterns = [
    path('/book', list_books, name= 'list_books'),
    path('/library', LibraryDetail.as_view(), name = 'LibraryDetail')
]
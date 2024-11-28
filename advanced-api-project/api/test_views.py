from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test123')
        self.client.login(username = 'test', password = 'test123')
        self.book_data = {
            'title' : 'TestBook',
            'author' : 'Testauthor',
            'publication_year' : '1990'
        }
        self.updated_book_data = {
            'title' : ' updatedBook',
            'author' : 'updated',
            'publication_year' : '1991'
        }

    def test_create_book(self):
        response = self.client.post('api/books/', self.book_data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.put('api/books/{book.id}/',self.updated_book_data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.delete('api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_permission_required(self):
        self.client.logout()
        response = self.client.post('api/books/', self.book_data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        
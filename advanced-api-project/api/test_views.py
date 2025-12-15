from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.urls import reverse
from .views import ListView 
from .models import Book, Author

class BookListTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Book 1", 
            author=self.author, 
            publication_year=2021
        )

    def test_list_books_view(self):
        url = reverse('list-book') 

        request = self.factory.get(url)

        response = ListView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
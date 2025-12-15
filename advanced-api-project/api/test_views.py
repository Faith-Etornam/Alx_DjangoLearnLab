from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    
    def setUp(self):
        # Creating test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        
        # Creating sample authors
        self.author_a = Author.objects.create(name='Author A')
        self.author_b = Author.objects.create(name='Author B')
        
        # Creating sample books
        self.book1 = Book.objects.create(title='Book One', author=self.author_a, publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author=self.author_b, publication_year=2021)
        self.book3 = Book.objects.create(title='Book Three', author=self.author_a, publication_year=2019)
        
        
    #-------- Test Listing Endpoint ----------
    def test_list_book(self):
        url = reverse('list-book')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)


    #-------- Test Filter Endpoint ----------
    def test_filter_books_by_author(self):
        url = reverse('list-book') + f'?author={self.author_a.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    #-------- Test Search Endpoint ----------
    def test_search_books_by_title(self):
        url = reverse('list-book') + '?search=Book Two'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book Two')


    #-------- Test Order Endpoint ----------
    def test_order_books_by_publication_year(self):
        url = reverse('list-book') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))


    #-------- Test Create Endpoint ----------
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('create-book')
        author_c = Author.objects.create(name='Author C')
        data = {'title': 'Book Four', 'author': author_c.id, 'publication_year': 2022}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        
    def test_create_book_unauthenticated(self):
        url = reverse('create-book')
        author_d = Author.objects.create(name='Author D')
        data = {'title': 'Book Five', 'author': author_d.id, 'publication_year': 2023}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_UNAUTHORIZED)


    # ----------- Test Update Endpoint -----------
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('update-book', args=[self.book1.id])
        data = {'title': 'Book One Updated'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Book One Updated')


    # ----------- Test Delete Endpoint -----------
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

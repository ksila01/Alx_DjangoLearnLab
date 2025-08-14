from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints (Task 3)
    Includes: list, detail, create, update, delete
    Also tests filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(title="Book Alpha", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Book Beta", publication_year=2021, author=self.author2)
        self.book3 = Book.objects.create(title="Python 101", publication_year=2022, author=self.author1)

    # -----------------------------
    # LIST VIEW TESTS
    # -----------------------------
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=Book Alpha'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book Alpha')

    def test_search_books_by_author(self):
        url = reverse('book-list') + '?search=Author Two'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author']['name'], 'Author Two')

    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check the first book has the latest year
        self.assertEqual(response.data[0]['publication_year'], 2022)

    # -----------------------------
    # DETAIL VIEW TEST
    # -----------------------------
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # -----------------------------
    # CREATE VIEW TEST
    # -----------------------------
    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        url = reverse('book-create')
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2023,
            'author': self.author2.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -----------------------------
    # UPDATE VIEW TEST
    # -----------------------------
    def test_update_book(self):
        url = reverse('book-update')
        data = {
            'id': self.book1.id,
            'title': 'Updated Book Title',
            'publication_year': 2020,
            'author': self.author1.id
        }
        response = self.client.put(url, data)
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book Title')

    # -----------------------------
    # DELETE VIEW TEST
    # -----------------------------
    def test_delete_book(self):
        url = reverse('book-delete')
        data = {'id': self.book2.id}
        response = self.client.delete(url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])
        self.assertEqual(Book.objects.count(), 2)

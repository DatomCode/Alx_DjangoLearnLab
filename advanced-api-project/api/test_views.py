from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
# Create your tests here.


class BookAPITests(APITestCase):
    
    def setUp(self):
        # 1. Create a user for authentication testing
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # 2. Create an author (required for creating books)
        self.author = Author.objects.create(name="J.K. Rowling")
        
        # 3. Create a book to use in read/update/delete tests
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        # 4. Define URLs for the API endpoints'
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    # --- CRUD TESTS ---

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data['title'], "Harry Potter and the Chamber of Secrets")

    def test_retrieve_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # We created 1 book in setUp, so length should be 1
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        data = {
            "title": "Harry Potter Updated",
            "publication_year": 1997,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db() # Refresh the object from the DB
        self.assertEqual(self.book.title, "Harry Potter Updated")

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # --- PERMISSION TESTS ---

    def test_create_book_unauthenticated(self):
        # We do NOT login here
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        # Expecting 403 Forbidden or 401 Unauthorized depending on settings
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- FILTERING, SEARCHING, ORDERING TESTS ---

    def test_filter_books_by_year(self):
        # Create a second book with a different year
        Book.objects.create(title="Old Book", publication_year=1950, author=self.author)
        
        # Filter for the year of the book created in setUp (1997)
        response = self.client.get(self.list_url, {'publication_year': 1997})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_search_books(self):
        Book.objects.create(title="Lord of the Rings", publication_year=1954, author=self.author)
        
        # Search for 'Harry'
        response = self.client.get(self.list_url, {'search': 'Harry'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Philosopher's Stone")

    def test_order_books(self):
        Book.objects.create(title="A Book", publication_year=2000, author=self.author)
        
        # Order by title
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 'A Book' should come before 'Harry Potter'
        self.assertEqual(response.data[0]['title'], "A Book")
        self.assertEqual(response.data[1]['title'], "Harry Potter and the Philosopher's Stone")
# api/views.py

from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# -----------------------------
# AUTHOR VIEWSET
# -----------------------------
class AuthorViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Author model.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can read; only authenticated can modify

# -----------------------------
# BOOK VIEWSET
# -----------------------------
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# -----------------------------
# GENERIC VIEWS FOR BOOK
# -----------------------------

# List all books (searchable)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # read-only for unauthenticated users
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only authenticated users can create

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

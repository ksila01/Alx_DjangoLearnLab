from rest_framework import viewsets, filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
# -----------------------------
# AUTHOR VIEWSET (Task 0)
# -----------------------------
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# -----------------------------
# BOOK VIEWSET (Task 0)
# -----------------------------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# -----------------------------
# GENERIC VIEWS FOR BOOK (Task 1 & 2)
# -----------------------------

class BookListView(generics.ListAPIView):
    """
    Lists all books with filtering, searching, and ordering capabilities.
    
    Features:
    - Filter by title, author, and publication_year
    - Search by title or author name
    - Order by title or publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Filtering backend
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Fields available for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Fields available for searching
    search_fields = ['title', 'author__name']
    
    # Fields available for ordering
    ordering_fields = ['title', 'publication_year']
    
    # Default ordering if not specified by user
    ordering = ['title']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

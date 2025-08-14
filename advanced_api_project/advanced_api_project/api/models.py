from django.db import models
from django.utils import timezone

# Author model - represents a book author
class Author(models.Model):
    # Name of the author
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model - represents a book written by an author
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)

    # Year the book was published
    publication_year = models.IntegerField()

    # Link to Author (One author can have many books)
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

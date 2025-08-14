from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    Includes validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year {value} cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    Includes a nested representation of related books.
    """
    # Nested serializer for the related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
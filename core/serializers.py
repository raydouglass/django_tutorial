from rest_framework.serializers import ModelSerializer
from .models import Author, Book

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'books']

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'year', 'authors']
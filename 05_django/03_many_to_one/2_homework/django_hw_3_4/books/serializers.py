from rest_framework import serializers
from .models import Book, Genre
from authors.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()

    def get_book_count(self, obj):
        return obj.book_count

    class Meta:
        model = Book
        fields = ('title', 'author', )


class GenreSerializer(serializers.ModelSerializer):
    class BookForGenreSerializer(serializers.ModelSerializer):
        author = AuthorSerializer(read_only=True)
        
        class Meta:
            model = Book
            fields = ('title', 'author', )

    books = BookForGenreSerializer(many=True, read_only=True)
    book_count = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ('name', 'books', 'book_count', )
    
    def get_book_count(self, obj):
        return obj.books.count()  # books는 related_name

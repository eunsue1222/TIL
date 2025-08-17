from rest_framework import serializers
from .models import Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'published_date', 'borrowed', 'isbn', 'genres']

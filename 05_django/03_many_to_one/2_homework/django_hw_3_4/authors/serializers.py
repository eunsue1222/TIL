from rest_framework import serializers
# from books.serializers import BookSerializer
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', )
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count
from .models import Book
from .serializers import BookSerializer

# Create your views here.
@api_view(['GET'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    book = Book.objects.annotate(book_count=Count('book')).get(pk=book_pk)
    serializers = BookSerializer(book)
    return Response(serializers.data)
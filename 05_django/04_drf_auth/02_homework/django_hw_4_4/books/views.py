from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


# 전체 리스트 조회 (인증 불필요)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ISBN 으로 상세 조회 (인증 불필요)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "isbn"   # 기본 pk 대신 isbn 으로 조회
    permission_classes = [permissions.AllowAny]


# 대여 (인증 필요)
class BorrowBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, isbn):   # ✅ URL 경로에서 isbn 받도록 수정
        try:
            book = Book.objects.get(isbn=isbn)
            book.borrowed = True
            book.save()

            serializer = BookSerializer(book)  # ✅ 책 정보 반환
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "해당 ISBN 도서가 존재하지 않습니다."},
                            status=status.HTTP_404_NOT_FOUND)

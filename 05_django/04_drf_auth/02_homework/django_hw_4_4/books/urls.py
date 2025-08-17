from django.urls import path
from .views import BookListView, BookDetailView, BorrowBookView

urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),
    path("api/<str:isbn>/", BookDetailView.as_view(), name="book-detail"),   # GET
    path("api/<str:isbn>/", BorrowBookView.as_view(), name="borrow-book"),   # POST
]

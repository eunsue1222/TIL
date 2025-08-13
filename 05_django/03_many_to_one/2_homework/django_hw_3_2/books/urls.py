from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_pk>/', views.book_detail),
]

from django.contrib import admin
from .models import Book, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','published_date','borrowed','isbn')
    search_fields = ('title','isbn')
    list_filter = ('borrowed','genres')
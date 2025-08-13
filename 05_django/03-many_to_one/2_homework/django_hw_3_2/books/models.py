from django.db import models
# from authors.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('authors.author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
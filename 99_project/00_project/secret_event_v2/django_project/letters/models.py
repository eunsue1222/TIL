from django.db import models

# name - content  
class Letter(models.Model):
    name = models.CharField()
    content = models.CharField()
    music = models.TextField()
    link = models.TextField()
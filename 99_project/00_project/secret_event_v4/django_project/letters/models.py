from django.db import models

# name - content  
class Letter(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField()
    music = models.CharField(max_length=100)
    music_content = models.CharField()
    image_link = models.URLField()
    music_link = models.URLField()
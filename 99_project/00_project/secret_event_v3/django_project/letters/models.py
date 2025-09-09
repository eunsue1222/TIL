from django.db import models

# name - content  
class Letter(models.Model):
    name = models.CharField()
    content = models.CharField()
    music_content = models.CharField()
    music = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)
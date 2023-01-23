from django.db import models

# Create your models here.

class Song(models.Model):

    title = models.TextField(blank=False)
    artist = models.TextField(blank=False, default="unknown")
    lyrics = models.TextField(blank=False, default="Unavailable")
    file_location = models.SlugField(blank=False,default="none")

    def __str__(self) -> str:
        return ("Title : " + str(self.title) + " Artist: " + str(self.artist))
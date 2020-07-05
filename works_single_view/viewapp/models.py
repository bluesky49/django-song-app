from django.db import models

class Song(models.Model):
    title = models.CharField(max_length = 100, blank=False)
    contributor = models.CharField(max_length = 100)
    iswc = models.CharField(max_length = 20, unique = True)

    def __str__(self):
        return self.title

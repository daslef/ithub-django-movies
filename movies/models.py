from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    filmed = models.DateField()
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.filmed.year})'
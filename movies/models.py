from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    filmed = models.DateField()
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.filmed.year})"


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    content = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.movie}] {self.content[:20]} ({self.created.day}.{self.created.month})"

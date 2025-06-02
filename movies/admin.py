from django.contrib import admin
from .models import Movie, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["movie", "content", "created"]
    list_filter = ["movie", "created"]
    search_fields = ["content"]


class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "filmed", "duration"]
    list_filter = ["created", "duration"]
    search_fields = ["title"]


admin.site.register(Movie, MovieAdmin)

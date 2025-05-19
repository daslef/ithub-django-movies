from django.contrib import admin
from .models import Movie



class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'filmed', 'duration']
    list_filter = ['created', 'duration']
    search_fields = ['title']

admin.site.register(Movie, MovieAdmin)

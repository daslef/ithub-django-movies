from django.views.generic import ListView, DetailView
from .models import Movie


class MoviesView(ListView):
    model = Movie
    paginate_by = 10
    template_name = "movies/index.html"


class MovieView(DetailView):
    model = Movie
    template_name = 'movies/detail.html'

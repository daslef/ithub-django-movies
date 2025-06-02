from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Movie


class MoviesView(ListView):
    model = Movie
    paginate_by = 10
    template_name = "movies/index.html"


class MovieView(DetailView):
    template_name = "movies/detail.html"
    model = Movie


# class MovieView(FormMixin, DetailView):
#     form_class = CreateCommentForm
#     model = Movie
#     template_name = "movies/detail.html"

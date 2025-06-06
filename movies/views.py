from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Movie, Review
from .forms import CreateReviewForm


class MoviesView(ListView):
    model = Movie
    paginate_by = 10
    template_name = "movies/index.html"


class MovieView(LoginRequiredMixin, FormMixin, DetailView):
    form_class = CreateReviewForm
    template_name = "movies/detail.html"
    model = Movie


@login_required
@require_POST
def add_review(request, pk):
    movie = Movie.objects.get(pk=pk)
    new_review_form = CreateReviewForm(request.POST)
    if new_review_form.is_valid():
        content = new_review_form.cleaned_data["content"]
        new_review = Review(content=content, movie=movie, author=request.user)
        new_review.save()
    return redirect("movie", pk=pk)

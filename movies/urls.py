from django.urls import path

from .views import MoviesView, MovieView, add_review

urlpatterns = [
    path("", MoviesView.as_view(), name="movies"),
    path("<int:pk>", MovieView.as_view(), name="movie"),
    path("<int:pk>/add_review", add_review, name="add_review")
]

from django.urls import path

from .views import MoviesView, MovieView

urlpatterns = [
    path("", MoviesView.as_view(), name="movies"),
    path("<int:pk>", MovieView.as_view(), name="movie"),
    # path("<int:pk>/add_comment", handle_add_comment, name="add_comment")
]

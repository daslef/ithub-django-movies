from django.views.generic import TemplateView


class MoviesView(TemplateView):
    template_name = "movies/index.html"

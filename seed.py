def main():
    movies = Movie.objects.all()
    print(f"There are {movies.count()} tasks in the database")


if __name__ == "__main__":
    import os
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    application = get_wsgi_application()

    from movies.models import Movie

    main()

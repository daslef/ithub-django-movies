from datetime import date
import faker


def main():
    faker_instance = faker.Faker(providers=[])

    movies = Movie.objects.all()
    initial_count = movies.count()

    for _ in range(10):
        title = faker_instance.text(15)

        Movie(
            title=title,
            slug=title.replace(' ', '-'),
            duration=faker_instance.random_number(3),
            filmed=faker_instance.date_between()
        ).save()
    
    print(f"There was {movies.count() - initial_count} movies added")



if __name__ == "__main__":
    import os
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
    application = get_wsgi_application()

    from movies.models import Movie

    main()

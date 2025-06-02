from django.forms import Form, CharField


class CreateReviewForm(Form):
    content = CharField(max_length=2000, required=True)

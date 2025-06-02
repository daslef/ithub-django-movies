from django.forms import Form, CharField, Textarea


class CreateReviewForm(Form):
    content = CharField(
        max_length=2000,
        required=True,
        label="Your review",
        widget=Textarea(attrs={"class": "entry"}),
    )

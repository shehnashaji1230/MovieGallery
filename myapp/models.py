from django.db import models

# Create your models here.

class GenreChoices(models.TextChoices):
    ACTION='Action','Action'
    FICTION='Fiction','Fiction'
    THRILLER='Thriller','Thriller'

class Movies(models.Model):

    title=models.CharField(max_length=200)

    genre=models.CharField(max_length=200,choices=GenreChoices.choices)

    language=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    director=models.CharField(max_length=200)
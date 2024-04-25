from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length = 255)
    duration = models.CharField(max_length = 255)
    grade = models.CharField(max_length = 255)
    poster_url = models.CharField(max_length = 2083)

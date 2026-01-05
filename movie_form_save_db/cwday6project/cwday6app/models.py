from django.db import models

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    release_year = models.IntegerField()    
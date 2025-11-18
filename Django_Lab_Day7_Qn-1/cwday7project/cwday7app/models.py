from django.db import models

class Library(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
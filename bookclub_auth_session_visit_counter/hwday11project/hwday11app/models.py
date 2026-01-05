from django.db import models

# Create your models here.
class book_club(models.Model):
    userName = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

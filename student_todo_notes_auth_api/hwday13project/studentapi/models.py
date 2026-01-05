from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


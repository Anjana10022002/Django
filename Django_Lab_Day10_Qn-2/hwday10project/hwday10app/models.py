from django.db import models

class student_record(models.Model):
    student_name = models.CharField(max_length=100)
    student_class = models.IntegerField()
    student_age = models.IntegerField()

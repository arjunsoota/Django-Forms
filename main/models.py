from django.db import models


# Create your models here.

class Student(models.Model):
    GENDERS=(
    ('f','female'),
    ('m','male')
    )
    name = models.CharField(max_length=256)
    roll_number = models.IntegerField()
    gender = models.CharField(max_length=1,choices=GENDERS)

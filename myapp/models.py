from django.db import models

# Create your models here.


class Patient(models.Model):
    first_name= models.CharField(max_length = 150)
    last_name=models.CharField(max_length=150)
    age=models.IntegerField()

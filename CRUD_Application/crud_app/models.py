from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    E_email=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    mobile=models.IntegerField()


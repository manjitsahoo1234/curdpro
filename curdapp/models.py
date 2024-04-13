from django.db import models
# Create your models here.
class StudentsData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    fee=models.IntegerField()
    assignment1=models.IntegerField()
    assignment2=models.IntegerField()
    assignment3=models.IntegerField()
    assignment4=models.IntegerField()
    institute=models.CharField(max_length=50)
    location=models.CharField(max_length=100)

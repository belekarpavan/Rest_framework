from django.db import models

# Create your models here.
class student(models.Model):
    roll=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    dob=models.DateField()
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
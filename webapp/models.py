from django.db import models

# Create your models here.

class employees(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.fname
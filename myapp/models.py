from django.db import models

# Create your models here.
class Registration(models.Model):
    employee_id = models.CharField(max_length=25)
    name        = models.CharField(max_length=25)
    email       = models.CharField(max_length=30)
    phone       = models.IntegerField()
    gender      = models.CharField(max_length=10)
    job         = models.CharField(max_length=50)
    image       = models.FileField(upload_to='Profilepic/')
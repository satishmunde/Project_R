from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone= models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField()


# Create your models here.

from django.db import models

class Developer(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField("Email")
    phone = models.CharField("Phone Number",max_length=10)
    position = models.CharField("Position",max_length=50)
    skills = models.TextField("Skills and Experience")
    image = models.ImageField(upload_to='images/',null=True,default=None)

# Create your models here.

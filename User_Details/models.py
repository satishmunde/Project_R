from django.db import models

class UserDtl(models.Model):
    # user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    fname = models.CharField("First_Name", max_length=50, blank=True,)
    lname = models.CharField("Last_Name", max_length=50, blank=True,)
    email = models.EmailField("Email")
    phoneNo = models.IntegerField("Phone Number")
    addressLine1 = models.TextField("Address Line 1")
    addressLine2 = models.TextField('Address Line 2')
    state = models.CharField('State',max_length=20)
    country = models.CharField(max_length=20)
    zipCode = models.PositiveSmallIntegerField()



# Create your models here.

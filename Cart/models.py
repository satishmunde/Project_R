from django.db import models
from django.contrib.auth.models import User

class UserCart(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE )
    itemid = models.IntegerField()
    orderid = models.PositiveBigIntegerField()
    status = models.CharField(max_length=20)




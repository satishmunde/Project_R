from django.db import models

class Item(models.Model):
    p_img = models.FileField(upload_to="Items/",max_length=250,null=True,default=None)
    p_title = models.CharField(max_length=100)
    p_desc = models.TextField()
    p_price = models.BigIntegerField()
    p_id = models.BigIntegerField()


       
# Create your models here.

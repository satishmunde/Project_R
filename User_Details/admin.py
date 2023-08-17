from django.contrib import admin
from User_Details.models import UserDtl

class UserInfo(admin.ModelAdmin):
    list_display = ('fname', 'lname','email','phoneNo','addressLine1','addressLine2','state','country','zipCode')
# Register your models here.

admin.site.register(UserDtl,UserInfo)
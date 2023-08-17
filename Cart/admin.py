from django.contrib import admin
from Cart.models import UserCart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'itemid',"orderid","status")
# Register your models here.
admin.site.register(UserCart,CartAdmin)

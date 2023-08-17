from django.contrib import admin
from django.contrib.admin.sites import site
from Items.models import Item

class ItemAdmin(admin.ModelAdmin):
    item_list=('p_img','p_title','p_desc','p_price','p_id')
admin.site.register(Item,ItemAdmin)


# Register your models here.

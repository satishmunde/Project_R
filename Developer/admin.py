from django.contrib import admin
from Developer.models import Developer

class DevAdmin(admin.ModelAdmin):
    Dev_list = ('name','email','phone','position','skills','image')

admin.site.register(Developer,DevAdmin)
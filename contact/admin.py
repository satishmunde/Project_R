from django.contrib import admin
from contact.models import ContactUs
class Contact(admin.ModelAdmin):
    list_display = ('name','phone','email','message')

# Register your models here.
admin.site.register(ContactUs,Contact)
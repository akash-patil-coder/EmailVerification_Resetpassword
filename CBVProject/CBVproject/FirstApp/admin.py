from django.contrib import admin
from .models import Laptop

# Register your models here.

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['lid','company','model_name','ram','rom','processor','price','weight']
admin.site.register(Laptop,LaptopAdmin)
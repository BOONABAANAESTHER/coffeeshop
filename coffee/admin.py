from django.contrib import admin
from .models import Coffee  

# Correct import of ModelAdmin
from django.contrib.admin import ModelAdmin

#This class allows you to customize the admin interface for your models
# Register your model with the admin site
class CoffeeAdmin(ModelAdmin):  
    list_display = ['name', 'price','quantity']  
admin.site.register(Coffee, CoffeeAdmin)

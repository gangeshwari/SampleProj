from django.contrib import admin

# Register your models here.
from .models import CellPhones, Laptops

admin.site.register(CellPhones)
admin.site.register(Laptops)

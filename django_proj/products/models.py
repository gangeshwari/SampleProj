from django.db import models

class CellPhones(models.Model):
    name = models.CharField(max_length=150, null=False)
    price = models.IntegerField(null=False)
    model = models.CharField(max_length=150, null=True)
    ram = models.CharField(max_length=150, null=True)
    rom = models.CharField(max_length=150, null=True)
    battery = models.CharField(max_length=150, null=True)
    rear_camera = models.CharField(max_length=150, null=True)
    front_camera = models.CharField(max_length=150, null=True)
    color = models.CharField(max_length=150, null=True)

class Laptops(models.Model):
    which_laptop = models.CharField(max_length=150, null=False)
    price = models.IntegerField(null=False)
    model = models.CharField(max_length=150, null=True)
    ram = models.CharField(max_length=150, null=True)
    rom = models.CharField(max_length=150, null=True)
    battery = models.CharField(max_length=150, null=True)
    sales_package = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=150, null=True)
    os = models.CharField(max_length=150, null=False)
    l_type = models.CharField(max_length=150, null=False)
    processor_type = models.CharField(max_length=150, null=False)
    processor_generation = models.CharField(max_length=150, null=False)

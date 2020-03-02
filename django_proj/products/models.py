from django.db import models

class CellPhones(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(max_length=200, null=False)
    model = models.CharField(max_length=200, null=True)

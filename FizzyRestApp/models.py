from django.db import models

class Manufacturer(models.Model):
    title = models.CharField(max_length=100, blank=False)
    yearFounded = models.IntegerField()
    imageUrl = models.CharField(max_length=200, blank=True)

class Drink(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=True, default='')
    calories = models.IntegerField()
    imageUrl = models.CharField(max_length=200, blank=True)
    manufacturer = models.ForeignKey(Manufacturer)

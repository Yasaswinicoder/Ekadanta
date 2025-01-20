# models.py

from django.db import models

class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=50)  # Vehicle brand
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vehicles/', default='vehicles/default.jpg')

    def __str__(self):
        return self.name
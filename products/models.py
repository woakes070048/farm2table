from django.db import models


# Create your models here.

class Product(models.Model):
    """The model for various products that farmers/producers sell"""
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=70)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField()

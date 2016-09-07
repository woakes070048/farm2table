from django.db import models


# Create your models here.

class Product(models.Model):
    """The model for various products that farmers/producers sell"""
    # TODO
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=70)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Override the str function to return the Product's name"""
        return self.name

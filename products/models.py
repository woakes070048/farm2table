import os
from django.contrib.auth.models import User
from django.db import models


def get_image_path(instance, filename):
    return os.path.join('products/media', str(instance.id), filename)


class Product(models.Model):
    """The model for various products that farmers/producers sell"""
    product_types = (
        ("V", "Vegetable"),
        ("F", "Fruit"),
        ("A", "Animal Product"),
        ("G", "Grain")
    )
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=2, choices=product_types, default="V")
    owner = models.ForeignKey(User, related_name="products")
    image = models.ImageField(blank=True, null=True, upload_to=get_image_path)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Override the str function to return the Product's name"""
        return self.name

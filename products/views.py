from django.shortcuts import render
from .models import Product


def list_products(request):
    """
    List products
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, "list.html", context)

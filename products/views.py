from django.shortcuts import render
from django.views.generic import DetailView
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


class ProductDetail(DetailView):
    """
    Individual product page
    """
    model = Product
    template_name = "product.html"

from django.shortcuts import render
from django.http import HttpResponse


def list_products(request):
    return HttpResponse("Welcome to the products page {}!".format(request.user.username))

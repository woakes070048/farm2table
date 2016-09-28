import factory
import factory.fuzzy
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Product


class UserFactory(factory.django.DjangoModelFactory):
    """
    Creates a standard user
    """

    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = first_name
    password = make_password("test")


class ProductFactory(factory.django.DjangoModelFactory):
    """
    Creates a product
    """
    CHOICES = [x[0] for x in Product.product_types]

    class Meta:
        model = Product

    name = factory.Faker("name")
    type = factory.fuzzy.FuzzyChoice(CHOICES)
    owner = factory.SubFactory(UserFactory)
    description = factory.Faker("text", max_nb_chars=300)
    quantity = 20

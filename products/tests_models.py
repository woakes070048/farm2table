from django.test import TestCase
from products.models import Product
from .factories import UserFactory, ProductFactory


class ProductTest(TestCase):
    def setUp(self):
        self.product = Product(name="test banana", type="test fruit", quantity="1", owner=UserFactory())
        self.product.save()

    def tearDown(self):
        self.product.delete()

    def test_string_method(self):
        self.assertEqual("test banana", self.product.__str__())

    def test_modified_field_is_updating(self):
        before = self.product.modified
        self.product.save()
        self.assertNotEqual(before, self.product.modified)

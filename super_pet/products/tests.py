from django.test import TestCase
from .models import Product

# Create your tests here.

def add(a,b):
    return a+b


class ProductTest(TestCase):
    def setUp(self):
        self.product = Product.cust_manager.create(product_name = "test product",
                                    product_description="description for test",
                                    product_price = 5000,
                                    product_brand = "superpet")


    def test_add(self):
        expected_answer = 17
        actual_answer = add(11,6)
        self.assertEqual(expected_answer,actual_answer)

    
    def test_add_product(self):
        product = Product.cust_manager.get(id = self.product.id)
        self.assertEqual(self.product,product)


    def test_all_products(self):
        products = Product.cust_manager.all()
        answer = len(products)>0
        self.assertTrue(answer)


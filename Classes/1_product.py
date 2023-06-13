"""
Product Inventory Project - Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand. Then create an inventory
class which keeps track of various products and can sum up the inventory value.

https://github.com/karan/Projects
"""

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    id: int
    quantity: int

class Inventory:

    def __init__(self):
        self.products = []
    
    def add_product(self, product: Product) -> None:
        self.products.append(product)
    
    def sum_products(self) -> float:
        return sum(product.price for product in self.products)
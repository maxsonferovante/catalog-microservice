from typing import List
from catalog_microservice.domain.models.products import Products



class ProductRepositorySpy:
    def __init__(self):    
        self.insert_product_atributes = {}
        self.select_product_atributes = {}

    def insert_product(self, name: str, description: str, price: float, category_id: int) -> None:
        self.insert_product_atributes['name'] = name
        self.insert_product_atributes['description'] = description
        self.insert_product_atributes['price'] = price
        self.insert_product_atributes['category_id'] = category_id
        return

    def select_product(self,  product_id: int) -> List[Products]:
        self.select_product_atributes['product_id'] = product_id
        return [Products(
            id=1,
            name='Product 1',
            description='Description 1',
            price=10.0,
            category_id=1
        )]

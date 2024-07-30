from typing import List
from catalog_microservice.domain.models.products import Products
from catalog_microservice.domain.models.categories import Categories


class ProductRepositorySpy:
    def __init__(self):    
        self.insert_product_atributes = {}
        self.select_product_atributes = {}

    def insert_product(self, name: str, description: str, price: float, stock: int, category_id: str) -> None:
        self.insert_product_atributes['name'] = name
        self.insert_product_atributes['description'] = description
        self.insert_product_atributes['price'] = price
        self.insert_product_atributes['stock'] = stock
        self.insert_product_atributes['category_id'] = category_id
        return

    def select_product(self,  product_id: str) -> List[Products]:
        self.select_product_atributes['product_id'] = product_id
        product = Products(
            id=1,
            name='Product 1',
            description='Description 1',
            price=10.0,
            stock=10,
            category_id=1
        )
        product.category = Categories(
            id=1,
            name='Category 1',
            description='Description 1'
        )
        return [product]

    def select_products(self) -> List[Products]:
        product1 = Products(
            id=1,
            name='Product 1',
            description='Description 1',
            price=10.0,
            stock=10,
            category_id=1
        )
        product1.category = Categories(
             id=1,
            name='Category 1',
            description='Description 1'
        )
        
        product2 = Products(
            id=2,
            name='Product 2',
            description='Description 2',
            price=20.0,
            stock=20,
            category_id=2
        )
        product2.category = Categories(
             id=2,
            name='Category 2',
            description='Description 2'
        )
        
        return [
            product1,
            product2]
        
    def select_products_by_ids(self, products_ids: List[str]) -> List[Products]:
        self.select_product_atributes['products_ids'] = products_ids
        product1 = Products(
            id=1,
            name='Product 1',
            description='Description 1',
            price=10.0,
            stock=10,
            category_id=1,
        )
        product1.updated_at = '2021-07-01T00:00:00Z'
        product1.category = Categories(
             id=1,
            name='Category 1',
            description='Description 1'
        )
        
        product2 = Products(
            id=2,
            name='Product 2',
            description='Description 2',
            price=20.0,
            stock=20,
            category_id=2
        )
        product2.updated_at = '2021-07-01T00:00:00Z'
        product2.category = Categories(
             id=2,
            name='Category 2',
            description='Description 2'
        )
        
        return [
            product1,
            product2]
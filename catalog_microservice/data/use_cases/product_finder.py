from typing import Dict, List

from catalog_microservice.domain.use_cases.product_finder_interface import ProductFinderInterface
from catalog_microservice.data.interfaces.product_repository_interface import ProductRepositoryInterface
from catalog_microservice.domain.models.products import Products

class ProductFinder(ProductFinderInterface):
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def find(self, product_id: int) -> Dict:
        self.__validate_product_id(product_id)
        products = self.__search_product(product_id)
        return self.__format_response(products)
    
    @classmethod
    def __validate_product_id(cls, product_id: int) -> Exception:
        if not product_id or type(product_id) != int:
            raise Exception("Product ID must be a number")
        if product_id < 0:
            raise Exception("Product ID must be a positive number")
        
    def __search_product(self, product_id: int) -> List[Products]:
        products = self.product_repository.select_product(product_id)                  
        if products == []:
            raise Exception("Product not found")
        return products
        
        
    def __format_response(self, products: List[Products]) -> Dict:
        attributes = []
        for product in products:
            attributes.append({
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'category_id': product.category_id
            })
        response = {
            'type': 'Products',
            'count': products.__len__(),
            'atributes': products
        }
        return response
from typing import Dict

from catalog_microservice.domain.use_cases.product_register_interface import ProductRegisterInterface
from catalog_microservice.data.interfaces.product_repository_interface import ProductRepositoryInterface
from catalog_microservice.domain.models.products import Products

from catalog_microservice.errors.types.http_unprocessable_content import HttpUnprocessableContentError

class ProductRegister(ProductRegisterInterface):
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def register(self, name: str, description: str, price: float, category_id: int) -> Dict:
        
        self.__validate_product(name, description, price, category_id)
        
        self.__create_product(name, description, price, category_id)      
        
        return self.__format_response(name, description, price, category_id)
    
    @classmethod
    def __validate_product(cls, name: str, description: str, price: float, category_id: int) -> Exception:
        if not name or type(name) != str:
            raise HttpUnprocessableContentError("Name must be a string")
        if not description or type(description) != str:
            raise HttpUnprocessableContentError("Description must be a string")
        if not price or type(price) != float:
            raise HttpUnprocessableContentError("Price must be a float")
        if not category_id or type(category_id) != int:
            raise HttpUnprocessableContentError("Category_id must be a integer")
        
    def __create_product(self, name: str, description: str, price: float, category_id: int) -> Products:
        self.product_repository.insert_product(
            name=name,
            description=description,
            price=price,
            category_id=category_id
        )
    
    @classmethod    
    def __format_response(self, name: str, description: str, price: float, category_id: int ) -> Dict:
        response = {
            'type': 'Products',
            'count': 1,
            'atributes': {
                'name': name,
                'description': description,
                'price': price,
                'category_id': category_id
            }
        }
        return response
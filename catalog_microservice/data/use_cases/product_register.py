from typing import Dict

from catalog_microservice.domain.use_cases.product_register_interface import ProductRegisterInterface
from catalog_microservice.data.interfaces.product_repository_interface import ProductRepositoryInterface
from catalog_microservice.domain.models.products import Products

from catalog_microservice.errors.types.http_unprocessable_content import HttpUnprocessableContentError

from catalog_microservice.infra.database.errors.types.category_not_found_error import CategoryNotFoundError
from catalog_microservice.infra.database.errors.types.database_error import DatabaseError

class ProductRegister(ProductRegisterInterface):
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def register(self, name: str, description: str, price: float, stock:int,  category_id: str) -> Dict:
        
        self.__validate_product(name, description, price, stock, category_id)
        
        product_result = self.__create_product(name, description, price, stock, category_id)      
        
        return self.__format_response(product_result)
    
    @classmethod
    def __validate_product(cls, name: str, description: str, price: float, stock:int, category_id: str) -> Exception:
        if not name or type(name) != str:
            raise HttpUnprocessableContentError("Name must be a string")
        if not description or type(description) != str:
            raise HttpUnprocessableContentError("Description must be a string")
        if not price or type(price) != float:
            raise HttpUnprocessableContentError("Price must be a float")
        if not stock or type(stock) != int or stock < 0:
            raise HttpUnprocessableContentError("Stock must be a integer greater than 0")
        if not category_id or type(category_id) != str:
            raise HttpUnprocessableContentError("Category_id must be a UUID string")
        
    def __create_product(self, name: str, description: str, price: float, stock:int, category_id: str) -> Products:
        try:
        
            product_id_result = self.product_repository.insert_product(
                name=name,
                description=description,
                price=price,
                stock=stock,
                category_id=category_id
            )
            
            return Products(
                id=product_id_result,
                name=name,
                price=price,
                stock=stock,
                description=description,
                category_id=category_id
            )
        except CategoryNotFoundError as e:
            raise HttpUnprocessableContentError(str(e))
        except DatabaseError as e:
            raise HttpUnprocessableContentError('An error occurred while processing your request: { }; Please try again later.'.format(str(e)))
        except Exception as e:
            raise e
    
    @classmethod    
    def __format_response(self, product: Products) -> Dict:
        response = {
            'type': 'Products',
            'count': 1,
            'atributes': {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'stock': product.stock,
                'category_id': product.category_id
            }
        }
        return response
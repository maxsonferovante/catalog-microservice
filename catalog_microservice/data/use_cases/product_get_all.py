from catalog_microservice.domain.use_cases.product_get_all_interface import ProductGetAllInterface
from catalog_microservice.data.interfaces.product_repository_interface import ProductRepositoryInterface
from catalog_microservice.domain.models.products import Products


class ProductGetAll(ProductGetAllInterface):
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def get_all(self) -> list:
        products = self.product_repository.select_products()
        
        return self.__forma_response(products)
    
    
    def __forma_response(self, products: list) -> dict:
        products_response = list(map(lambda product: {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'stock': product.stock,
            'price': product.price,
            'category': {
                'id': product.category.id,
                'name': product.category.name,
                'description': product.category.description
            }
            }, products))

      
        response = {
            'type': 'Products',
            'count': products.__len__(),
            'atributes': products_response
        }
        return response
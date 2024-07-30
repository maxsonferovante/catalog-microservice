from typing import List

from catalog_microservice.domain.use_cases.product_get_stock_interface import ProductGetStockInterface
from catalog_microservice.data.interfaces.product_repository_interface import ProductRepositoryInterface


class ProductGetStockUseCase(ProductGetStockInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.product_repository = product_repository

    def get_stock(self, products_ids: List[str]) -> dict:
        
        products = self.product_repository.select_products_by_ids(products_ids)

        return self.__format_response(products)

    def __format_response(self, products) -> List[dict]:
        products_response = list(map(lambda product: {
            'id': product.id,
            'name': product.name,            
            'stock': product.stock,
            'updated_at': product.updated_at,
        }, products))

        response = {
            'type': 'Products',
            'count': products.__len__(),
            'atributes': products_response
        }
        return response
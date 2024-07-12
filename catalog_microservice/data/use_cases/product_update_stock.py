from datetime import datetime

from catalog_microservice.domain.use_cases.product_update_stock_interface import ProductUpdateStockInterface
from catalog_microservice.data.interfaces.product_repository_interface import ProductRepositoryInterface

from catalog_microservice.infra.database.errors.types.product_not_found_error import ProductNotFoundError
from catalog_microservice.infra.database.errors.types.database_error import DatabaseError

from catalog_microservice.errors.types.http_not_found import HttpNotFoundError

class ProductUpdateStock(ProductUpdateStockInterface):
    def __init__(self, product_repository:ProductRepositoryInterface):
        self.product_repository = product_repository

    def update_stock(self, product_id: str, stock: int):
        
        self.__validate_stock(stock)
        
        self.__update_stock(product_id, stock)
        
        return self.__return_success(product_id, stock)
                
    def __validate_stock(self, stock):
        if type(stock) != int or stock < 0:
            raise ValueError("Stock must be a non-negative integer")
        
    def __update_stock(self, product_id, stock):
        try:
            product = self.product_repository.select_product(product_id)
            
            if product.stock - stock < 0:
                raise ValueError("Stock cannot be negative for product with id {}".format(product_id))
            
            self.product_repository.update_stock(product_id, stock)
        except ProductNotFoundError as e:
            raise HttpNotFoundError(str(e))
        except DatabaseError as e:
            raise e
        except Exception as e:
            raise e
            
    def __return_success(self, product_id, stock):
        return {
            'status': 'success',
            'message': 'Stock of product with id {} updated to {}.'.format(product_id, stock),
            'timestamp': datetime.now().isoformat()
        }
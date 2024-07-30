from abc import ABC, abstractmethod
from typing import List

from catalog_microservice.domain.models.products import Products

class ProductRepositoryInterface(ABC):
    @abstractmethod
    def insert_product(self, name: str, description: str, price: float, category_id: str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def select_product(self, product_id: str) -> Products:
        raise NotImplementedError     
    
    @abstractmethod
    def select_products(self) -> List[Products]:
        raise NotImplementedError
    
    @abstractmethod
    def update_stock(self, product_id: str, stock: int):
        raise NotImplementedError
    
    @abstractmethod
    def select_products_by_ids(self, products_id: List[str]) -> List[Products]:
        raise NotImplementedError
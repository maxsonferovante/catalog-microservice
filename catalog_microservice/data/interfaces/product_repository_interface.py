from abc import ABC, abstractmethod
from typing import List

from catalog_microservice.domain.models.products import Products

class ProductRepositoryInterface(ABC):
    @abstractmethod
    def insert_product(self, name: str, description: str, price: float, category_id: int) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def select_product(self, product_id: int) -> List[Products]:
        raise NotImplementedError     
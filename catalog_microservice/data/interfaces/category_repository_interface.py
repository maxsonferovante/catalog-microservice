from abc import ABC, abstractmethod
from typing import List

from catalog_microservice.domain.models.categories import Categories

class CategoryRepositoryInterface(ABC):
    @abstractmethod
    def insert_category(self, name: str, description:str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def select_category(self, category_id: str) -> List[Categories]:
        raise NotImplementedError     
    
    @abstractmethod
    def select_categories(self) -> List[Categories]:
        raise NotImplementedError
    
    @abstractmethod
    def update_category(self, category_id: str, name: str, description: str) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete_category(self, category_id: str) -> None:
        raise NotImplementedError
from abc import ABC, abstractmethod
from typing import Dict

class ProductFinderInterface(ABC):
    @abstractmethod
    def find(self, product_id: int) -> Dict:
        raise NotImplementedError

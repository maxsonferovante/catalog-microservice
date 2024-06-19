from abc import ABC, abstractmethod
from typing import Dict

class ProductRegisterInterface(ABC):
    @abstractmethod
    def register(self, name: str, description: str, price: float,category_id: int) -> Dict:
        raise NotImplementedError

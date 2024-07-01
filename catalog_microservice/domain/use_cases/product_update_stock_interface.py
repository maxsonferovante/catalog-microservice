from abc import ABC, abstractmethod
from typing import Dict


class ProductUpdateStockInterface(ABC):
    @abstractmethod
    def update_stock(self, product_id: str, stock: int) -> Dict:
        pass
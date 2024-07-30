from abc import ABC, abstractmethod
from typing import List


class ProductGetStockInterface(ABC):
    @abstractmethod
    def get_stock(self, products_ids: List[str]) -> List[dict]:
        raise NotImplementedError
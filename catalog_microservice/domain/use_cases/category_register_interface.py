from abc import ABC, abstractmethod
from typing import Dict


class CategoryRegisterInterface(ABC):
    @abstractmethod
    def register(self, name: str, description: str) -> Dict:
        raise NotImplementedError
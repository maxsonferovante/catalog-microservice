from abc import ABC, abstractmethod

class ProductGetAllInterface(ABC):
    @abstractmethod
    def get_all(self) -> list:
        raise NotImplementedError
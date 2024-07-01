from abc import ABC, abstractmethod

class KafkaRepositoryInterface(ABC):
    @abstractmethod
    def send_message(self, topic: str, key:str, value:str) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def consume_message(self, topic: str) -> any:
        raise NotImplementedError
    
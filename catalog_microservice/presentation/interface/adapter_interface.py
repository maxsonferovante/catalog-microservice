from abc import ABC, abstractmethod



class AdapterConsumerInterface(ABC):
    
    @abstractmethod
    def consume_messagens(self, topic: str):
        raise NotImplementedError
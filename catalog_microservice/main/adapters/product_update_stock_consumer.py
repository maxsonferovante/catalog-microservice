import json

from catalog_microservice.infra.messaging.entities.topics import Topics
from catalog_microservice.presentation.interface.adapter_interface import AdapterConsumerInterface
from catalog_microservice.infra.messaging.entities.message import Message

class ProductUpdateStockConsumer(AdapterConsumerInterface):
    
    def __init__(self, use_case, repository) -> None:
        self.use_case = use_case
        self.repository = repository
        
    
    def consume_messagens(self, topic: str):
        
        consumer = self.repository.get_consumer()
        consumer.subscribe([topic])
        try:
            while True:
                try:
                    message = self.repository.consume_message(
                        consumer = consumer,
                        topic = topic)
                    
                    if message is not None:
                        result = self.__process_message(message)                                                
                        self.repository.send_message(
                            topic= Topics.PRODUCT_STOCK_UPDATED.value,
                            key= message.key,
                            value= json.dumps(result))                        
                    else: 
                        pass                            
                except Exception as e:
                    print (e)
        except KeyboardInterrupt:
            print ("Exiting...")
        except Exception as e:
            print (e)
            raise e
        finally:
            consumer.close()
        
    def __process_message(self, message: Message):
        return self.use_case.update_stock(message.value.get('product_id'), message.value.get('stock'))
        
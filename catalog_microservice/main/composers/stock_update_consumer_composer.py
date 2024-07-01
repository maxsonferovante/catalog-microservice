from functools import wraps

from catalog_microservice.infra.messaging.repositories.kafka_repository import KafkaRepository
from catalog_microservice.infra.database.repositories.products_repository import ProductRepository

from catalog_microservice.data.use_cases.product_update_stock import ProductUpdateStock
from catalog_microservice.main.adapters.product_update_stock_consumer import ProductUpdateStockConsumer



message_consumers = {} # type: Dict[str, ProductUpdateStockConsumer]

def stock_update_consumer_composer(topic: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            repository = KafkaRepository()
            
            product_repository = ProductRepository()
            
            product_update_stock_use_case = ProductUpdateStock(product_repository=product_repository)
            
            consumer_instance = ProductUpdateStockConsumer(
                use_case=product_update_stock_use_case,
                repository=repository)
            
            message_consumers[topic] = consumer_instance
            
            func(consumer_instance, *args, **kwargs)
        return wrapper
    return decorator
        
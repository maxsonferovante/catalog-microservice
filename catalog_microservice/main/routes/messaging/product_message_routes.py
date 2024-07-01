from catalog_microservice.infra.messaging.entities.topics import Topics

from catalog_microservice.main.composers.stock_update_consumer_composer import stock_update_consumer_composer
from catalog_microservice.main.adapters.product_update_stock_consumer import ProductUpdateStockConsumer


from catalog_microservice.errors.types.http_not_found import HttpNotFoundError

@stock_update_consumer_composer(topic=Topics.PRODUCT_UPDATE_STOCK.value)
def consumer_stock_update(consumer: ProductUpdateStockConsumer):    
    try:
    
        consumer.consume_messagens(topic=Topics.PRODUCT_UPDATE_STOCK.value)
    except Exception as e:
        print(e)
    
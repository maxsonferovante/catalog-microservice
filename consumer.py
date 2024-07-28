from catalog_microservice.infra.messaging.repositories.kafka_repository import KafkaRepository
from catalog_microservice.infra.messaging.entities.topics import Topics


def apresentationMessage(message):
    print (f"Key: {message.key} - Value: {message.value}")

def consumer_update_stock():
    kafkaRepository = KafkaRepository()
    
    consumer = kafkaRepository.get_consumer()
    consumer.subscribe([Topics.PRODUCT_STOCK_UPDATED.value])    
    while True:
        message = kafkaRepository.consume_message(            
                consumer = consumer,
                topic= Topics.PRODUCT_STOCK_UPDATED.value)
        if message is not None:
            apresentationMessage(message)
        else:
            print ("No message")
            
            
if __name__ == "__main__":
    consumer_update_stock()
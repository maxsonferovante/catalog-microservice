from typing import AsyncGenerator
from confluent_kafka import KafkaException
from catalog_microservice.data.interfaces.kafka_repository_interface import KafkaRepositoryInterface
from catalog_microservice.infra.messaging.settings.message_broker_connection import MessageBrokerConnectionHandler, MessageBrokerConnectionType
from catalog_microservice.infra.messaging.errors.types.kafka_connection_error import KafkaConnectionError

from catalog_microservice.infra.messaging.entities.message import Message

def callback_error(err, msg):
    if err is not None:
        print ("Failed to deliver message: {} - {}".format(msg.value(), err.str()))
    else: 
        print ("Message produced: {}".format(msg.str()))
        
class KafkaRepository(KafkaRepositoryInterface):
    
    @classmethod
    def send_message(cls, topic: str, key:str,value:str) -> None:
        with MessageBrokerConnectionHandler(MessageBrokerConnectionType.PRODUCER) as connection_handler:
            try:
                connection_handler.get_broker().produce(
                    topic=topic,
                    key=key,
                    value=value
                )
                connection_handler.get_broker().flush()        
            except KafkaException as e:
                raise KafkaConnectionError(f"Error sending message to Kafka: {e}")
            except Exception as e:
                raise e
    
    @classmethod
    def consume_message(cls, consumer,  topic: str):
        try:
            message = consumer.poll(timeout=1.0)
            if message is None:
                return
            if message.error():                
                    print ("No more messages. {} - {}".format(message.topic(), message.partition()))                
                    return
            else:   
                return Message(message)                        
        except KafkaException  as e:
            raise KafkaConnectionError(f"Error consuming message from Kafka: {e.message}")
        except Exception as e:
            raise e
            
    @classmethod
    def get_consumer(cls):
        with MessageBrokerConnectionHandler(MessageBrokerConnectionType.CONSUMER) as connection_handler:
            return connection_handler.get_broker()        
import os
from dotenv import load_dotenv
from confluent_kafka import KafkaException
from confluent_kafka.admin import AdminClient, NewTopic
from catalog_microservice.data.interfaces.kafka_repository_interface import KafkaRepositoryInterface
from catalog_microservice.infra.messaging.settings.message_broker_connection import MessageBrokerConnectionHandler, MessageBrokerConnectionType
from catalog_microservice.infra.messaging.errors.types.kafka_connection_error import KafkaConnectionError

from catalog_microservice.infra.messaging.entities.message import Message
from catalog_microservice.infra.messaging.entities.topics import Topics

load_dotenv()

def callback_error(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg.value())))
        
class KafkaRepository(KafkaRepositoryInterface):
    
    def __init__(self) -> None:
        self.__connection_string = "{}:{}/".format(
            os.environ["MESSAGE_BROKER_HOST"],
            os.environ["MESSAGE_BROKER_PORT"]
        )
        self.__create_topics()
    
    def __create_topics(self):
        try:
            admin = AdminClient({"bootstrap.servers": self.__connection_string})    
            topic_product_update_stock = NewTopic(Topics.PRODUCT_UPDATE_STOCK.value)
            topic_product_stock_updated = NewTopic(Topics.PRODUCT_STOCK_UPDATED.value)
            
            admin.create_topics([topic_product_update_stock, topic_product_stock_updated])
        except KafkaException as e:
            raise KafkaConnectionError(f"Error creating topics: {e}")
        except Exception as e:
            raise e
        
        return None
    @classmethod
    def send_message(cls, topic: str, key:str,value:str) -> None:
        with MessageBrokerConnectionHandler(MessageBrokerConnectionType.PRODUCER) as connection_handler:
            try:
                connection_handler.get_broker().produce(
                    topic=topic,
                    key=key,
                    value=value,
                    callback=callback_error                    
                )
                connection_handler.get_broker().poll(1)
                      
            except KafkaException as e:
                raise KafkaConnectionError(f"Error sending message to Kafka: {e}")
            except Exception as e:
                raise e
    
    @classmethod
    def consume_message(cls, consumer,  topic: str):
        try:
            message = consumer.poll(timeout=0.5)
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
import socket
import os
import uuid
from dotenv import load_dotenv
from enum import Enum
from confluent_kafka import Consumer, Producer

load_dotenv()

""" 
    A class that handles the connection to the message broker.
"""
class MessageBrokerConnectionType(Enum):
    PRODUCER = 1
    CONSUMER = 2


class MessageBrokerConnectionHandler:
    def __init__(self, type: MessageBrokerConnectionType) -> None:
        self.__connection_string = "{}:{}/".format(
            os.environ["MESSAGE_BROKER_HOST"],
            os.environ["MESSAGE_BROKER_PORT"]
        )
        self.topic = os.environ["MESSAGE_BROKER_TOPIC"] + str(uuid.uuid4())
        self.broker = self.__create_broker(type)

    def __create_broker(self, type: MessageBrokerConnectionType):
        try:
            if type == MessageBrokerConnectionType.PRODUCER:
                print (self.__connection_string, socket.gethostname())
                return Producer({"bootstrap.servers": self.__connection_string, "client.id": socket.gethostname()})
            elif type == MessageBrokerConnectionType.CONSUMER:
                return Consumer({
                    "bootstrap.servers": self.__connection_string,
                    "group.id": self.topic,
                    })
        except ValueError:    
            raise ValueError("Invalid connection type. Use 'MessageBrokerConnectionType.PRODUCER' or 'MessageBrokerConnectionType.CONSUMER'")
        except Exception as e:
            raise e
    
    def get_broker(self):
        return self.broker
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.broker = None
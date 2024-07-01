import json
from catalog_microservice.infra.messaging.errors.types.encode_message_error import EncodeMessageError
from catalog_microservice.infra.messaging.errors.types.create_object_message_error import CreateObjectMessageError

class Message:
    def __init__(self,message):
        self.topic = None
        self.key = None
        self.value = None
        self.create_object_message(message)
        
    def to_string(self):
        return json.dumps(self.to_dict())
    
    def to_dict(self):
        return {
            'topic': self.topic,    
            'key': self.key,
            'value': self.value
        }
    def create_object_message(self, message):
        try:            
            self.topic = message.topic()
            self.key = message.key().decode('utf-8')   
            self.value = json.loads(message.value().decode('utf-8'))        
        except EncodeMessageError as e:
            print (e)
            raise e        
        except Exception as e:
            print (e)
            raise CreateObjectMessageError(topic=message.topic())
    

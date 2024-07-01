

class KafkaConnectionError(Exception):
    def __init__(self, message: str):
        super().__init__("Error to connect to Kafka: {}".format(message))
        self.message = message
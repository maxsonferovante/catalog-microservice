

class CreateObjectMessageError(Exception):
    def __init__(self, topic: str):
        super().__init__("Error to create object message for topic: {}".format(topic))
        self.topic = topic
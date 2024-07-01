

class EncodeMessageError(Exception):
    def __init__(self, topic: str):
        super().__init__("Error to encode message for topic: {}".format(topic))
        self.topic = topic
from catalog_microservice.main.routes.messaging.product_message_routes import consumer_stock_update

class ServerMessaging:
        
        def __init__(self) -> None:
            pass
        
        def start_message_consumers(self):
            consumer_stock_update()
            
        def start_message_producers(self):
            pass    




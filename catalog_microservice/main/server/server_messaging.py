from multiprocessing import Process
from catalog_microservice.main.routes.messaging.product_message_routes import consumer_stock_update

class ServerMessaging:
        
        def __init__(self) -> None:
            self.list_consumer = []
            self.list_process = []
        def add_consumer(self, consumer):
            self.list_consumer.append(consumer)
            
        def run(self):
            self.list_process = [Process(target=consumer_stock_update, name= consumer.__name__) 
                                 for consumer in self.list_consumer]
            for process in self.list_process:
                print ("Starting process {}".format(process.name))
                process.start()
                print ("Process {} started".format(process.name))

        def stop(self):
            for process in self.list_process:
                process.terminate()
                process.join()
                print ("Process {} stopped".format(process.name))
            
        



server_messaging = ServerMessaging()
server_messaging.add_consumer(consumer=consumer_stock_update)

import http.client
import json
import random
import time 
from catalog_microservice.infra.messaging.repositories.kafka_repository import KafkaRepository
from catalog_microservice.infra.messaging.entities.topics import Topics

kafkaRepository = KafkaRepository()

def request_get_all_products():
    # http://localhost:8000/products/all
    client = http.client.HTTPConnection(host= 'localhost', port=8001, timeout=30)
    
    client.request('GET', '/products/all')
    
    response = client.getresponse()
    
    if response.status == 200:
        print ("Response status: ", response.status)
        
        response = response.read()
        
        response = response.decode('utf-8')
        
        return json.loads(response)
    else:    
        print ("Error: ", response.status)
        return None

def producer_update_stock(key, value):    
    response = kafkaRepository.send_message(Topics.PRODUCT_UPDATE_STOCK.value, key=key, value=value)
    
def new_stock_random():
    return random.randrange(1)

def main():
    
    while True:
        data = request_get_all_products()    
            
        if data['data']['count'] == 0:
            print ("No products to update stock")

        list_products = data['data']['atributes'] 
        
        for product in list_products:
            new_stock = new_stock_random()
                
            print ("Run producer_update_stock() for product: {} and old stock: {} / new stock: {}".format(product['id'], product['stock'], new_stock))
                
            value = json.dumps({
                    'product_id': product['id'],
                    'stock': new_stock
                })
            
            producer_update_stock(key=product['id'], value=value)            
    


if __name__ == '__main__':
    try:
        
        main()
            
    except KeyboardInterrupt:
        print ("Bye!")
        exit(0)
    except Exception as e:
        print ("Error: ", e)
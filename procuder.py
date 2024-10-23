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
        data = { 
                "data": {
		    "atributes": [
                {
                    "category": {
                        "description": "Synchronized composite algorithm",
                        "id": "840be210-7e19-5f93-b997-43d3c6ed8fb4",
                        "name": "Clothing"
                    },
                    "description": "Operative next generation circuit",
                    "id": "00b4f388-4a16-50ac-9ab9-be13fdd3f87b",
                    "name": "Salad",
                    "price": "42.00",
                    "stock": 44
                },
                {
                    "category": {
                        "description": "Object-based local structure",
                        "id": "46fe8de9-94a7-5ffc-9f0c-8e700e26fc9e",
                        "name": "Tools"
                    },
                    "description": "Profit-focused disintermediate process improvement",
                    "id": "0163690f-5007-51fe-b14d-ab9462cfeecb",
                    "name": "For repair Cotton Gloves",
                    "price": "72.00",
                    "stock": 12
                },
                {
                    "category": {
                        "description": "Centralized value-added customer loyalty",
                        "id": "df83e778-efa9-5c10-a786-4597ac44bbed",
                        "name": "Shoes"
                    },
                    "description": "Focused foreground success",
                    "id": "01898931-1c02-5ba2-ab92-0584774a3e83",
                    "name": "Car",
                    "price": "1.00",
                    "stock": 19
                },
                {
                    "category": {
                        "description": "Re-engineered scalable parallelism",
                        "id": "c786db45-4659-5b6e-90e6-7e964f1971c8",
                        "name": "Computers"
                    },
                    "description": "Cross-platform cohesive standardization",
                    "id": "01cbaab7-08e0-572d-8734-dd8752d34f36",
                    "name": "Fantastic Plastic Table",
                    "price": "86.00",
                    "stock": 44
                },
                {
                    "category": {
                        "description": "Extended zero tolerance budgetary management",
                        "id": "8303098f-0034-5a83-9432-d0511324b537",
                        "name": "Outdoors"
                    },
                    "description": "Open-source tertiary orchestration",
                    "id": "0202f162-0ee2-58e3-90a7-f55a5e5ab96e",
                    "name": "Fantastic Plastic Keyboard",
                    "price": "48.00",
                    "stock": 79
                },
                {
                    "category": {
                        "description": "Synergistic systemic benchmark",
                        "id": "26035f81-1e2a-5a50-83cd-82d294834fcb",
                        "name": "Industrial"
                    },
                    "description": "Multi-channeled disintermediate info-mediaries",
                    "id": "02c7391e-2fc3-52c2-aaa8-7a1be0f2ec06",
                    "name": "Metal Ball",
                    "price": "86.00",
                    "stock": 28
                },
            ],	
            "count": 500,
		    "type": "Products"
	    }
        }
            
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
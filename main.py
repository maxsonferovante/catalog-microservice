import os
from dotenv import load_dotenv
from threading import Thread
from catalog_microservice.app import FlaskApp
from catalog_microservice.main.server.server import app
from catalog_microservice.main.server.server_messaging import server_messaging

if __name__ == '__main__':
    load_dotenv()  
    options = {
        'workers': os.environ['NUM_WORKERS']
    }
    print (options)
    
    try:
        server_messaging.run()
        FlaskApp( app=app, options=options).run()
    except Exception as e:
        print (e)
        server_messaging.stop()
        raise e
    finally:
        server_messaging.stop()
        print ("Server stopped")
    
    
    
    
     
    
    
    

    

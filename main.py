import os
import concurrent.futures
from dotenv import load_dotenv
from catalog_microservice.app import FlaskApp
from catalog_microservice.main.server.server import app
from catalog_microservice.main.server.server_messaging import ServerMessaging

def main():
    load_dotenv()  
    options = {
        'bind': os.environ['BIND_HOST_PORT'],
        'workers': os.environ['NUM_WORKERS']
    }
    print (options)
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        
        future_server_message = executor.submit(ServerMessaging().start_message_consumers)
        
        future_server_flask = executor.submit(FlaskApp( app=app, options=options).run())
        
        concurrent.futures.wait([future_server_message, future_server_flask])   

if __name__ == '__main__':
    main()
    
    
    
     
    
    
    

    

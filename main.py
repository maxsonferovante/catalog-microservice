from dotenv import load_dotenv
import os

from catalog_microservice.app import FlaskApp
from catalog_microservice.main.server.server import app

if __name__ == '__main__':
    load_dotenv()        
    options = {
        'bind': os.environ['BIND_HOST_PORT'],
        'workers': os.environ['NUM_WORKERS']
    }
    print (options)
    FlaskApp(
        app=app,
        options=options
    ).run()
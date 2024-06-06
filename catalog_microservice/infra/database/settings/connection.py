# This file contains the class that will handle the connection to the database
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from dotenv import load_dotenv
import os

load_dotenv()

"""
    A class that handles the database connection settings.
"""
class DBConnectionHandler:  

    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            os.environ["DB_ENGINE"],
            os.environ["DB_USER"],
            os.environ["DB_PASSWORD"],
            os.environ["DB_HOST"],
            os.environ["DB_PORT"],
            os.environ["DB_NAME"]
        )
        self.__engine = self.__create_engine()
        
        
    def __create_engine(self) -> Engine:
        return create_engine(self.__connection_string)
     
    def get_engine(self) -> Engine:
        return self.__engine 
    
    
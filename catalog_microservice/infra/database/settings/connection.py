# This file contains the class that will handle the connection to the database
import os
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from catalog_microservice.infra.database.settings.base import Base


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
        self.session = None
        
        Base.metadata.create_all(self.__engine)
        
    def __create_engine(self) -> Engine:
        return create_engine(self.__connection_string)
     
    def get_engine(self) -> Engine:
        return self.__engine 
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.session = None
    

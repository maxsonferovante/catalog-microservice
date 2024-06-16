from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Numeric, String

from catalog_microservice.infra.database.settings.base import Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from catalog_microservice.infra.database.entities.category import Category


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric(10, 2))
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, autoincrement=True, default=datetime.now)
    updated_at = Column(DateTime, autoincrement=True, default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return f'Product(id={self.id}, name={self.name}, description={self.description}'
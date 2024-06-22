from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Numeric, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from catalog_microservice.infra.database.settings.base import Base
from catalog_microservice.infra.database.entities.categorys import Categorys


class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Numeric(10, 2))
    
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    
    created_at = Column(DateTime, autoincrement=True, default=datetime.now)
    updated_at = Column(DateTime, autoincrement=True, default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return f'Product(id={self.id}, name={self.name}, description={self.description}'
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from catalog_microservice.infra.database.settings.base import Base

class Categorys(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True, type_=Integer, autoincrement=True)
    
    name = Column(String(255))
    description = Column(String(255))
    created_at = Column(DateTime, autoincrement=True, default=datetime.now)
    updated_at = Column(DateTime, autoincrement=True, default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return f'Category(id={self.id}, name={self.name}, description={self.description})'
    
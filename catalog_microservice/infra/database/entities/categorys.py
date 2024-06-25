from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from catalog_microservice.infra.database.settings.base import Base

class Categories(Base):
    __tablename__ = 'categories'
    id: Mapped[str] = mapped_column(String(225),primary_key=True)
    
    name = Column(String(255))
    description = Column(String(255))
    created_at = Column(DateTime, autoincrement=True, default=datetime.now)
    updated_at = Column(DateTime, autoincrement=True, default=datetime.now, onupdate=datetime.now)
    
    products = relationship("Products", back_populates="category")

    def __repr__(self):
        return f'Category(id={self.id}, name={self.name}, description={self.description})'
    
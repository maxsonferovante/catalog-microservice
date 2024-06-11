from sqlalchemy import Column, Integer, String, DateTime
from catalog_microservice.infra.database.settings.base import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, current_timestamp=True)
    updated_at = Column(DateTime, current_timestamp=True)
    
    def __repr__(self):
        return f'Category(id={self.id}, name={self.name}, description={self.description})'
from typing import List

from catalog_microservice.infra.database.settings.connection import DBConnectionHandler
from catalog_microservice.infra.database.entities.product import Product as ProductEntity
from catalog_microservice.domain.interfaces.product_repository_interface import ProductRepositoryInterface
# from catalog_microservice.domain.models.product import Products



class ProductRepository():
    
    @classmethod
    def insert_product(cls, name: str, description: str, price: float, category_id: int) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_product = ProductEntity(name=name, description=description, price=price, category_id=category_id)
                db_connection.session.add(new_product)
                db_connection.session.commit()
            except Exception as e:
                db_connection.session.rollback()
                raise e
        
    @classmethod
    def select_product(cls, name: str):
        with DBConnectionHandler() as db_connection:
            try:
                products = (
                    db_connection.session
                    .query(ProductEntity)
                    .filter(ProductEntity.name == name)
                    .all()
                )
                return products
            except Exception as e:
                db_connection.session.rollback()
                raise e
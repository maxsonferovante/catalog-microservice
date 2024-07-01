from sqlalchemy.orm import joinedload
from typing import List
from catalog_microservice.infra.utils.generate_uuid import generate_uuid
from catalog_microservice.infra.database.settings.connection import DBConnectionHandler
from catalog_microservice.infra.database.entities.products import Products as ProductsEntity
from catalog_microservice.infra.database.entities.categorys import Categories as CategoriesEntity
from catalog_microservice.data.interfaces.product_repository_interface import ProductRepositoryInterface

from catalog_microservice.domain.models.products import Products

from catalog_microservice.infra.database.errors.types.product_not_found_error import ProductNotFoundError
from catalog_microservice.infra.database.errors.types.category_not_found_error import CategoryNotFoundError
from catalog_microservice.infra.database.errors.types.database_error import DatabaseError
class ProductRepository(ProductRepositoryInterface):
    
    @classmethod
    def insert_product(cls, name: str, description: str, price: float, stock:int, category_id: str) -> str:
        with DBConnectionHandler() as db_connection:
            try:
                
                category_exists  = db_connection.session.query(CategoriesEntity).filter(CategoriesEntity.id == category_id).first()
                if not category_exists:
                    raise CategoryNotFoundError(category_id=category_id)
                                
                new_product = ProductsEntity(id= generate_uuid(), name=name, description=description, price=price, stock= stock, category_id=category_id)    
                db_connection.session.add(new_product)
                db_connection.session.commit()
                return new_product.id
                
            except CategoryNotFoundError as e:
                db_connection.session.rollback()
                raise e
            except IntegrityError as e:
                db_connection.session.rollback()
                raise DatabaseError('Database integrity error occurred.')
            except Exception as e:
                db_connection.session.rollback()
                raise DatabaseError('An unexpected error occurred: {}'.format(e))
        
    @classmethod
    def select_product(cls,  product_id: str) -> List[Products]:
        with DBConnectionHandler() as db_connection:
            try:
                products = (
                    db_connection.session
                    .query(ProductsEntity)
                    .filter(ProductsEntity.id == product_id)
                    .all()
                )
                return products
            except Exception as e:
                db_connection.session.rollback()
                raise e
    
    @classmethod
    def select_products(cls) -> List[Products]:
        with DBConnectionHandler() as db_connection:
            try:
                products = (
                    db_connection.session
                    .query(ProductsEntity)
                    .options(joinedload(ProductsEntity.category))
                    .order_by(ProductsEntity.created_at.desc())
                    .all()
                    
                )
                return products
            except Exception as e:
                db_connection.session.rollback()
                raise e
    
    @classmethod
    def update_stock(cls, product_id: str, stock: int):
        with DBConnectionHandler() as db_connection:
            try:
                product = db_connection.session.query(ProductsEntity).filter(ProductsEntity.id == product_id).first()
                if not product:
                    raise ProductNotFoundError(product_id=product_id)
                product.stock = stock
                db_connection.session.commit()
            except ProductNotFoundError as e:
                db_connection.session.rollback()
                raise e
            except Exception as e:
                db_connection.session.rollback()
                raise DatabaseError('An unexpected error occurred: {}'.format(e))
            
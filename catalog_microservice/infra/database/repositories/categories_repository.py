from typing import List

from catalog_microservice.infra.utils.generate_uuid import generate_uuid
from catalog_microservice.infra.database.settings.connection import DBConnectionHandler
from catalog_microservice.infra.database.entities.categorys import Categorys as CategoriesEntity
from catalog_microservice.data.interfaces.category_repository_interface import CategoryRepositoryInterface

from catalog_microservice.domain.models.categories import Categories

from catalog_microservice.infra.database.errors.types.category_not_found_error import CategoryNotFoundError
from catalog_microservice.infra.database.errors.types.database_error import DatabaseError

class CategoryRepository(CategoryRepositoryInterface):
    
    @classmethod
    def insert_category(cls, name: str, description: str) -> str:
        with DBConnectionHandler() as db_connection:
            try:
                new_category = CategoriesEntity(id=generate_uuid(), name=name, description=description)
                db_connection.session.add(new_category)
                db_connection.session.commit()
                return new_category.id
            except IntegrityError as e:
                db_connection.session.rollback()
                raise DatabaseError('Database integrity error occurred.')
            except Exception as e:
                db_connection.session.rollback()
                raise DatabaseError('An unexpected error occurred: {}'.format(e))
            
    @classmethod
    def select_category(cls, category_id: str) -> List[Categories]:
        with DBConnectionHandler() as db_connection:
            try:
                category = (
                    db_connection.session
                    .query(CategoriesEntity)
                    .filter(CategoriesEntity.id == category_id)
                    .all()
                )
                return category
            except Exception as e:
                db_connection.session.rollback()
                raise e
    
    @classmethod
    def select_categories(cls) -> List[Categories]:
        with DBConnectionHandler() as db_connection:
            try:
                categories = (
                    db_connection.session
                    .query(CategoriesEntity)
                    .order_by(CategoriesEntity.created_at.desc())
                    .all()
                )
                return categories
            except Exception as e:
                db_connection.session.rollback()
                raise e
    
    @classmethod
    def update_category(cls, category_id: str, name: str, description: str) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                category = (
                    db_connection.session
                    .query(CategoriesEntity)
                    .filter(CategoriesEntity.id == category_id)
                    .first()
                )
                if not category:
                    raise CategoryNotFoundError(category_id=category_id)
                
                category.name = name
                category.description = description
                
                db_connection.session.commit()
            except CategoryNotFoundError as e:
                db_connection.session.rollback()
                raise e
            except Exception as e:
                db_connection.session.rollback()
                raise DatabaseError('An unexpected error occurred: {}'.format(e))
    
    @classmethod
    def delete_category(cls, category_id: str) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                category = (
                    db_connection.session
                    .query(CategoriesEntity)
                    .filter(CategoriesEntity.id == category_id)
                    .first()
                )
                if not category:
                    raise CategoryNotFoundError(category_id=category_id)
                db_connection.session.delete(category)
                db_connection.session.commit()
            except CategoryNotFoundError as e:
                db_connection.session.rollback()
                raise e
            except Exception as e:
                db_connection.session.rollback()
                raise DatabaseError('An unexpected error occurred: {}'.format(e))
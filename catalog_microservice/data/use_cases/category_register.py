from typing import Dict

from catalog_microservice.domain.use_cases.category_register_interface import CategoryRegisterInterface
from catalog_microservice.data.interfaces.category_repository_interface import CategoryRepositoryInterface

from catalog_microservice.domain.models.categories import Categories

from catalog_microservice.infra.database.errors.types.category_not_found_error import CategoryNotFoundError
from catalog_microservice.infra.database.errors.types.database_error import DatabaseError

class CategoryRegister(CategoryRegisterInterface):
    def __init__(self, category_repository: CategoryRepositoryInterface):
        self.category_repository = category_repository

    def register(self, name: str, description: str) -> Dict:
        
        self.__validate_category(name, description)
        
        category_result = self.__create_category(name, description)      
        
        return self.__format_response(category_result)
    
    @classmethod
    def __validate_category(cls, name: str, description: str) -> Exception:
        if not name or type(name) != str:
            raise HttpUnprocessableContentError("Name must be a string")
        if not description or type(description) != str:
            raise HttpUnprocessableContentError("Description must be a string")
        
    def __create_category(self, name: str, description: str) -> Categories:
        try:
        
            category_id_result = self.category_repository.insert_category(
                name=name,
                description=description
            )
            return Categories(
                category_id_result,
                name,
                description
            )
        except DatabaseError as e:
            raise HttpUnprocessableContentError('An error occurred while processing your request: { }; Please try again later.'.format(str(e)))
        except Exception as e:
            raise e
    
    @classmethod    
    def __format_response(self, category: Categories) -> Dict:
        response = {
            'type': 'Categories',
            'count': 1,
            'atributes': {
                'id': category.id,
                'name': category.name,
                'description': category.description
            }
        }
        
        return response
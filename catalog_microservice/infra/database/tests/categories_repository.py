from typing import List

from catalog_microservice.domain.models.categories import Categories

class CategoryRepositorySpy:
    def __init__(self):    
        self.insert_category_atributes = {}
        self.select_category_atributes = {}
        self.select_categories_atributes = {}
        self.update_category_atributes = {}
        
    def insert_category(self, name: str, description: str) -> None:
        self.insert_category_atributes['name'] = name
        self.insert_category_atributes['description'] = description
        return
    
    def select_category(self, category_id: str) -> List[Categories]:
        self.select_category_atributes['category_id'] = category_id
        return [Categories(
            id=1,
            name='Category 1',
            description='Description 1'
        )]
        
    def select_categories(self) -> List[Categories]:
        return [
            Categories(
                id='uuid string 1',
                name='Category 1',
                description='Description 1'
            ),
            Categories(
                id='uuid string 1',
                name='Category 2',
                description='Description 2'
            )
        ]
        
    def update_category(self, category_id: str, name: str, description: str) -> None:
        self.update_category_atributes['category_id'] = category_id
        self.update_category_atributes['name'] = name
        self.update_category_atributes['description'] = description
        return
    
    def delete_category(self, category_id: str) -> None:
        self.delete_category_atributes['category_id'] = category_id
        return
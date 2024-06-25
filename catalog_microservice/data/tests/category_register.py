from typing import Dict

class CategoryRegisterSpy:
    def __init__(self) -> None:
        self.register_attributes = {}

    def register(self, name: str, description: str) -> Dict:
        self.register_attributes[name] = {
            'name': name
        }
        self.register_attributes[name]['description'] = description

        return {
            'type': 'Categories',
            'count': 1,
            'attributes': [
                {   
                    'id': 'uuid string', # 'id': 'uuid string
                    'name': 'category name',
                    'description': 'category description'
                }
            ]
        }
    
    
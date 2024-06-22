from typing import Dict

class ProductGetAllSpy:
    def __init__(self) -> None:
        self.get_all_attributes = {}
        
    def get_all(self) -> Dict:
        return {
            'type': 'Products',
            'count': 2,
            'attributes': [
                {
                    'name': 'Product 1',
                    'description': 'Description 1',
                    'price': 10.0,
                    'category_id': 1
                },
                {
                    'name': 'Product 2',
                    'description': 'Description 2',
                    'price': 20.0,
                    'category_id': 2
                }
            ]
        }
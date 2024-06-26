from typing import Dict

class ProductFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, product_id: str) -> Dict:
        self.find_attributes['product_id'] = product_id
        return {
            'type': 'Products',
            'count': 1,
            'attributes': [
                {
                    'name': 'product name',
                    'description': 'product description',
                    'price': 10.0,
                    'stock': 10,
                    'category_id': 1
                }
            ]
        }
    
  
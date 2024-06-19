from typing import Dict


class ProductRegisterSpy:
    def __init__(self) -> None:
        self.register_attributes = {}

    def register(self, name: str, description: str, price: float, category_id: int) -> Dict:
                
        self.register_attributes[name] = {
            'name': name,
            'description': description,
            'price': price,
            'category_id': category_id
        }
        
        return {
            'type': 'Products',
            'count': 1,
            'attributes': [
                {   
                    'name': 'product name',
                    'description': 'product description',
                    'price': 10.0,
                    'category_id': 1
                }
            ]
        }
      
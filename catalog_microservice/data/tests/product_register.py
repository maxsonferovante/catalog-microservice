from typing import Dict


class ProductRegisterSpy:
    def __init__(self) -> None:
        self.register_attributes = {}

    def register(self, name: str, description: str, price: float, stock: int, category_id: str) -> Dict:
                
        self.register_attributes[name] = {
            'name': name,
            'description': description,
            'price': price,
            'stock': stock,
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
                    'stock': 10,
                    'category_id': 1
                }
            ]
        }
      
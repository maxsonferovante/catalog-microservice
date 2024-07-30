from typing import List

class ProductGetStockSpy:
    def __init__(self):
        self.products_ids = []

    def get_stock(self, products_ids: List) -> List[dict]:
        return {
            'type': 'Products',
            'count': 1,
            'attributes': [
                {   
                    'id': 'uuid string',
                    'name': 'product name',
                    'stock': 10,
                    'updated_at': '2021-07-01T00:00:00Z'
                },
                {   
                    'id': 'uuid string',
                    'name': 'product name',
                    'stock': 10,
                    'updated_at': '2021-07-01T00:00:00Z'
                }
            ]
        }
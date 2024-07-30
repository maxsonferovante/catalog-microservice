from catalog_microservice.data.tests.product_get_stock import ProductGetStockSpy
from catalog_microservice.presentation.controller.product_get_stock_controller import ProductGetStockController


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {
            'products_ids': ['uuid string', 'uuid string']
        }

class HttpRequestMockError:
    def __init__(self) -> None:
        self.body = {
            'products_ids': ['uuid string not valid', 'uuid string']
        }
        
def test_product_get_stock_controller():
    productGetStockSpy = ProductGetStockSpy()
    
    product_get_stock_controller = ProductGetStockController(
        productGetStockSpy
    )
    
    http_request_mock = HttpRequestMock()
    response = product_get_stock_controller.handle(http_request_mock)
    
    assert response.status_code == 200
    assert response.body == {
        'data': {
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
    }
    
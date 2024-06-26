from catalog_microservice.presentation.controller.product_get_all_controller import ProductGetAllController
from catalog_microservice.data.tests.product_get_all import ProductGetAllSpy



class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {}
        
def test_product_get_all_controller():
    productGetAllSpy = ProductGetAllSpy()
    
    product_get_all_controller = ProductGetAllController(
        productGetAllSpy
    )
    
    assert product_get_all_controller is not None
    
def test_product_get_all_controller_handle():
    productGetAllSpy = ProductGetAllSpy()
    
    product_get_all_controller = ProductGetAllController(
        productGetAllSpy
    )
    
    http_request_mock = HttpRequestMock()
    
    response = product_get_all_controller.handle(http_request_mock)
    assert response.status_code == 200
    assert response.body == {
        'data': {
            'type': 'Products',
            'count': 2,
            'attributes': [
                {
                    'name': 'Product 1',
                    'description': 'Description 1',
                    'price': 10.0,
                    'stock': 10,
                    'category_id': 1
                },
                {
                    'name': 'Product 2',
                    'description': 'Description 2',
                    'price': 20.0,
                    'stock': 10,
                    'category_id': 2
                }
            ]
        }
    }
    
    assert productGetAllSpy.get_all_attributes == {}
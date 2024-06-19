from catalog_microservice.presentation.controller.product_register_controller import ProductRegisterController
from catalog_microservice.data.tests.product_register import ProductRegisterSpy


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {
            'name': 'product name',
            'description': 'product description',
            'price': 10.0,
            'category_id': 1
        }
        
class HttpRequestMockError:
    def __init__(self) -> None:
        self.body = {
            'name': 'product name',
            'description': 'product description',
            'price': 10.0
        }
        
def test_product_register_controller():
    productRegisterSpy = ProductRegisterSpy()
    
    product_register_controller = ProductRegisterController(
        productRegisterSpy
    )
    
    assert product_register_controller is not None

def test_product_register_controller_handle():
    productRegisterSpy = ProductRegisterSpy()
    
    product_register_controller = ProductRegisterController(
        productRegisterSpy
    )
    
    http_request_mock = HttpRequestMock()
    
    response = product_register_controller.handle(http_request_mock)
    assert response.status_code == 201
    assert response.body == {
        'data': {
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
    }
    
    assert productRegisterSpy.register_attributes == {
        'product name': {
            'name': 'product name',
            'description': 'product description',
            'price': 10.0,
            'category_id': 1
        }
    }
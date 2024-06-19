from catalog_microservice.presentation.controller.product_finder_controller import ProductFinderController

from catalog_microservice.data.tests.product_finder import ProductFinderSpy

class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {
            'product_id': 1 
        }
        
        
def test_product_finder_controller():
    productFinderSpy = ProductFinderSpy()
    
    product_finder_controller = ProductFinderController(
        productFinderSpy
    )
    
    assert product_finder_controller is not None
    

def test_product_finder_controller_handle():
    productFinderSpy = ProductFinderSpy()
    
    product_finder_controller = ProductFinderController(
        productFinderSpy
    )
    
    http_request_mock = HttpRequestMock()
    
    response = product_finder_controller.handle(http_request_mock)
    
    assert response.status_code == 200
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
    
    assert productFinderSpy.find_attributes == {
        'product_id': 1
    }
  
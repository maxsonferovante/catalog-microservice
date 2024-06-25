from catalog_microservice.data.tests.category_register import CategoryRegisterSpy
from catalog_microservice.presentation.controller.categoty_register_controller import CategoryRegisterController



class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {
            'name': 'category name',
            'description': 'category description'
        }

class HttpRequestMockError:
    def __init__(self) -> None:
        self.body = {
            'name': 'category name'
        }

def test_category_register_controller():
    categoryRegisterSpy = CategoryRegisterSpy()
    
    category_register_controller = CategoryRegisterController(
        categoryRegisterSpy
    )
    
    assert category_register_controller is not None
    
def test_category_register_controller_handle():
    categoryRegisterSpy = CategoryRegisterSpy()
    
    category_register_controller = CategoryRegisterController(
        categoryRegisterSpy
    )
    
    http_request_mock = HttpRequestMock()
    
    response = category_register_controller.handle(http_request_mock)
    assert response.status_code == 201
    assert response.body == {
        'data': {
            'type': 'Categories',
            'count': 1,
            'attributes': [
                {   
                    'id': 'uuid string',
                    'name': 'category name',
                    'description': 'category description'
                }
            ]
        }
    }
    
    assert categoryRegisterSpy.register_attributes['category name'] == {
        'name': 'category name',
        'description': 'category description'
    }
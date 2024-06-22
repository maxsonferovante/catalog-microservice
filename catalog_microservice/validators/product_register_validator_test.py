from catalog_microservice.validators.product_register_validator import product_register_validator



class MockRequest:
    def __init__(self) -> None:
        self.json = None
        

def test_product_register_validator():
    request = MockRequest()
    request.json = {
        'name': 'product test',
        'description': 'description test',
        'price': 10.0,
        'category_id': 1
    }
    
    response = product_register_validator(request)
    assert response is None

def test_product_register_validator_empty_name():
    request = MockRequest()
    request.json = {
        'name': '',
        'description': 'description test',
        'price': 10.0,
        'category_id': 1
    }
    
    try:
        product_register_validator(request)
    except Exception as e:
         assert str(e) == "{'name': ['empty values not allowed']}"         
        
    
def test_product_register_validator_empty_description():
    request = MockRequest()
    request.json = {
        'name': 'product test',
        'description': '',
        'price': 10.0,
        'category_id': 1
    }
    
    response = product_register_validator(request)
    assert response is None

def test_product_register_validator_empty_price():
    request = MockRequest()
    request.json = {
        'name': 'product test',
        'description': 'description test',
        'price': '',
        'category_id': 1
    }
    
    try:
        product_register_validator(request)
    except Exception as e:
         assert str(e) == "{'price': ['must be of float type']}"
         
def test_product_register_validator_empty_category_id():
    request = MockRequest()
    request.json = {
        'name': 'product test',
        'description': 'description test',
        'price': 10.0,
        'category_id': ''
    }
    
    try:
        product_register_validator(request)
    except Exception as e:
         assert str(e) == "{'category_id': ['must be of integer type']}"
         
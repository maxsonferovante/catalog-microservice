from catalog_microservice.validators.product_register_validator import product_register_validator
from catalog_microservice.infra.utils.generate_uuid import generate_uuid



class MockRequest:
    def __init__(self) -> None:
        self.json = None
        

def test_product_register_validator():
    request = MockRequest()
    request.json = {
        'name': 'product test',
        'description': 'description test',
        'price': 10.0,
        'stock': 10,
        'category_id': generate_uuid()
    }
    
    response = product_register_validator(request)
    assert response is None

def test_product_register_validator_empty_name():
    request = MockRequest()
    request.json = {
        'name': '',
        'description': 'description test',
        'price': 10.0,
        'stock': 10,
        'category_id': generate_uuid()
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
        'stock': 10,
        'category_id': generate_uuid()
    }
    try:
        response = product_register_validator(request)
    except Exception as e:
            assert str(e) == "{'description': ['empty values not allowed']}"
    

def test_product_register_validator_empty_price():
    request = MockRequest()
    request.json = {
        'name': 'product test',
        'description': 'description test',
        'price': '',
        'stock': 10,
        'category_id': generate_uuid()
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
        'stock': 10,
        'category_id': ''
    }
    
    try:
        product_register_validator(request)
    except Exception as e:
         assert str(e) == "{'category_id': ['empty values not allowed']}"

def test_product_register_validator_empty_stock():
    request = MockRequest()
    request.json = {
        'name': 'product test',
        'description': 'description test',
        'price': 10.0,
        'stock': '',
        'category_id': generate_uuid()
    }
    
    try:
        product_register_validator(request)
    except Exception as e:
         assert str(e) == "{'stock': ['must be of integer type']}"
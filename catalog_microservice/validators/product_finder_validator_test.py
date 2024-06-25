from catalog_microservice.validators.product_finder_validator import product_finder_validator
from catalog_microservice.infra.utils.generate_uuid import generate_uuid


class MockRequest:
    def __init__(self) -> None:
        self.args = None
        

def test_product_finder_validator():
    request = MockRequest()
    request.args = {
        'product_id': generate_uuid()
    }
    
    try:
        product_finder_validator(request)
    except Exception as e:
        assert str(e) == "{'product_id': ['The product_id must be an UUID string']}"
    
def test_product_finder_validator_empty_product_id():
    request = MockRequest()
    request.args = {
        'product_id': ''
    }
    
    try:
        product_finder_validator(request)
    except Exception as e:
        assert str(e) == "{'product_id': ['empty values not allowed']}"
    
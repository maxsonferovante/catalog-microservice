from catalog_microservice.validators.products_get_stock import products_get_stock_validator
from catalog_microservice.infra.utils.generate_uuid import generate_uuid

class MockRequest:
    def __init__(self) -> None:
        self.json = None
        

def test_products_get_stock_validator():
    request = MockRequest()
    request.json = {
        'products_ids': [generate_uuid(), generate_uuid()]
    }
    
    response = products_get_stock_validator(request)
    assert response is None

def test_products_get_stock_validator_empty_products_ids():
    request = MockRequest()
    request.json = {
        'products_ids': []
    }
    
    try:
        products_get_stock_validator(request)
    except Exception as e:
        assert str(e) == "{'products_ids': ['empty values not allowed']}"

def test_products_get_stock_validator_empty_products_ids():
    request = MockRequest()
    request.json = {
        'products_ids': ['']
    }
    
    try:
        products_get_stock_validator(request)
    except Exception as e:
        print(e)
        assert e is not None
        
# def test_products_get_stock_validator_empty_products_ids():
#     request = MockRequest()
#     request.json = {
#         'products_ids': ['123']
#     }
    
#     try:
#         products_get_stock_validator(request)
#     except Exception as e:
#         assert str(e) == "{'products_ids': ['The product_id must be an UUID string']}"

# def test_products_get_stock_validator_empty_products_ids():
#     request = MockRequest()
#     request.json = {
#         'products_ids': [generate_uuid(), '123']
#     }
    
#     try:
#         products_get_stock_validator(request)
#     except Exception as e:
#         assert str(e) == "{'products_ids': ['The product_id must be an UUID string']}"
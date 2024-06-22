from catalog_microservice.validators.product_finder_validator import product_finder_validator



class MockRequest:
    def __init__(self) -> None:
        self.args = None
        

def test_product_finder_validator():
    request = MockRequest()
    request.args = {
        'product_id': '1'
    }
    
    response = product_finder_validator(request)
    assert response is None
    
def test_product_finder_validator_empty_product_id():
    request = MockRequest()
    request.args = {
        'product_id': ''
    }
    
    try:
        product_finder_validator(request)
    except Exception as e:
        assert str(e) == "{'product_id': ['empty values not allowed']}"
    
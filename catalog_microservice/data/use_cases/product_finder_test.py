from catalog_microservice.infra.database.tests.products_repository import ProductRepositorySpy
from catalog_microservice.data.use_cases.product_finder import ProductFinder
from catalog_microservice.infra.utils.generate_uuid import generate_uuid
def test_find_with_product_not_found():
    product_repository = ProductRepositorySpy()
    
    product_finder = ProductFinder(product_repository)
    
    try:
        product_finder.find(generate_uuid())
    except Exception as e:
        assert str(e) == 'Product not found'    
        
def test_find_with_invalid_product_repository():
    try:
        ProductFinder(None)
    except Exception as e:
        assert str(e) == 'Product repository is required'
        
def test_find():
    product_repository = ProductRepositorySpy()
    
    product_finder = ProductFinder(product_repository)
    
    product_id = generate_uuid()
    response = product_finder.find(product_id=product_id)
    
    assert product_repository.select_product_atributes['product_id'] == product_id
    
    assert response == {
        'type': 'Products',
        'count': 1,
        'atributes': [
            {
                'name': 'Product 1',
                'description': 'Description 1',
                'price': 10.0,
                'category_id': 1
            }
        ]
    }
    

def test_find_with_invalid_product_id():
    product_repository = ProductRepositorySpy()
    
    product_finder = ProductFinder(product_repository)
      
    try:
        product_finder.find('1')
    except Exception as e:
        assert str(e) == 'Product ID must be a UUID string'
            

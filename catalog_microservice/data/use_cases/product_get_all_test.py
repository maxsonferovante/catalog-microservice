from catalog_microservice.infra.database.tests.products_repository import ProductRepositorySpy
from catalog_microservice.data.use_cases.product_get_all import ProductGetAll

def test_get_all_products():
    product_repository = ProductRepositorySpy()
    product_get_all = ProductGetAll(product_repository)
    
    response = product_get_all.get_all()
    
    assert response['type'] == 'Products'
    assert response['count'] > 0
    assert 'atributes' in response
    assert len(response['atributes']) > 0
    
 

   
    


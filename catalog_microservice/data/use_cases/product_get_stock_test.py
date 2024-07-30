from catalog_microservice.infra.database.tests.products_repository import ProductRepositorySpy
from catalog_microservice.data.use_cases.product_get_stock import ProductGetStockUseCase


def test_products_get_stock():
    product_repository = ProductRepositorySpy()
    
    products_get_stocks = ProductGetStockUseCase(product_repository)
    
    response = products_get_stocks.get_stock(['uuid string', 'uuid string'])
    
    
    assert response['type'] == 'Products'
    assert response['count'] > 0
    assert 'atributes' in response
    assert len(response['atributes']) > 0
    
    

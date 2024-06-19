from catalog_microservice.infra.database.tests.products_repository import ProductRepositorySpy
from catalog_microservice.data.use_cases.product_register import ProductRegister

from catalog_microservice.infra.database.repositories.products_repository import ProductRepository

def test_register_product():
    product_repository = ProductRepositorySpy()
    product_register = ProductRegister(product_repository)
    response = product_register.register(
        name='product',
        description='description',
        price=10.0,
        category_id=1
    )
    assert response['type'] == 'Products'
    assert response['count'] == 1
    assert response['atributes']['name'] == 'product'
    assert response['atributes']['description'] == 'description'
    assert response['atributes']['price'] == 10.0
    assert response['atributes']['category_id'] == 1
    
def test_register_product_with_invalid_name():
    product_repository = ProductRepositorySpy()
    product_register = ProductRegister(product_repository)
    try:
        product_register.register(
            name=None,
            description='description',
            price=10.0,
            category_id=1
        )
    except Exception as e:
        assert str(e) == 'Name must be a string'
        
    try:
        product_register.register(
            name=1,
            description='description',
            price=10.0,
            category_id=1
        )
    except Exception as e:
        assert str(e) == 'Name must be a string'

def test_register_product_with_invalid_description():
    product_repository = ProductRepositorySpy()
    product_register = ProductRegister(product_repository)
    try:
        product_register.register(
            name='product',
            description=None,
            price=10.0,
            category_id=1
        )
    except Exception as e:
        assert str(e) == 'Description must be a string'
        
    try:
        product_register.register(
            name='product',
            description=1,
            price=10.0,
            category_id=1
        )
    except Exception as e:
        assert str(e) == 'Description must be a string'

def test_register_product_with_invalid_price():
    product_repository = ProductRepositorySpy()
    product_register = ProductRegister(product_repository)
    try:
        product_register.register(
            name='product',
            description='description',
            price=None,
            category_id=1
        )
    except Exception as e:
        assert str(e) == 'Price must be a float'
        
    try:
        product_register.register(
            name='product',
            description='description',
            price='10.0',
            category_id=1
        )
    except Exception as e:
        assert str(e) == 'Price must be a float'
        
def test_register_product_with_invalid_category_id():
    product_repository = ProductRepositorySpy()
    product_register = ProductRegister(product_repository)
    try:
        product_register.register(
            name='product',
            description='description',
            price=10.0,
            category_id=None
        )
    except Exception as e:
        assert str(e) == 'Category_id must be a integer'
        
    try:
        product_register.register(
            name='product',
            description='description',
            price=10.0,
            category_id='1'
        )
    except Exception as e:
        assert str(e) == 'Category_id must be a integer'

def test_register_product_with_invalid_product_repository():
    try:
        ProductRegister(None)
    except Exception as e:
        assert str(e) == 'Product repository is required'
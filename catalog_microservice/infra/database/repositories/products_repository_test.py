import pytest
from sqlalchemy import text
from catalog_microservice.infra.database.settings.connection import DBConnectionHandler
from products_repository import ProductRepository


@pytest.mark.skip(reason="Sensive test")
def test_insert_product():
    db_connection_handler = DBConnectionHandler()
    connection = db_connection_handler.get_engine().connect()

    mocked_first_product = {
        "name": "Product 1",
        "description": "Description of product 1",
        "price": 10.0,
        "category_id": 1
    }
    
    products_repository = ProductRepository()
    products_repository.insert_product(
        name=mocked_first_product["name"],
        description=mocked_first_product["description"],
        price=mocked_first_product["price"],
        category_id=mocked_first_product["category_id"]
    )
    
    sql = '''
        SELECT * FROM products 
        WHERE name = '{}' 
        AND description = '{}'
        AND price = {}
    '''.format(
        mocked_first_product["name"],
        mocked_first_product["description"],
        mocked_first_product["price"]
    )
    
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    
    
    assert registry.name == mocked_first_product["name"]
    assert registry.description == mocked_first_product["description"]
    assert registry.price == mocked_first_product["price"]
    
    connection.execute(
        text(
            f'''
            DELETE FROM products WHERE id = {registry.id}
            '''
        )
    )
    connection.commit()
    connection.close()
    
   
@pytest.mark.skip(reason="Sensive test")
def test_select_product():
    db_connection_handler = DBConnectionHandler()
    connection = db_connection_handler.get_engine().connect()

    mocked_first_product = {
        "name": "Product 1",
        "description": "Description of product 1",
        "price": 10.0,
        "category_id": 1
    }
    
    products_repository = ProductRepository()
    products_repository.insert_product(
        name=mocked_first_product["name"],
        description=mocked_first_product["description"],
        price=mocked_first_product["price"],
        category_id=mocked_first_product["category_id"]
    )
    
    product = products_repository.select_product(product_id=1)
    
    assert product[0].name == mocked_first_product["name"]
    assert product[0].description == mocked_first_product["description"]
    assert product[0].price == mocked_first_product["price"]
    
    connection.execute(
        text(
            f'''
            DELETE FROM products WHERE id = {product[0].id}
            '''
        )
    )
    connection.commit()
    connection.close()
    
@pytest.mark.skip(reason="Sensive test")
def test_select_products():
    db_connection_handler = DBConnectionHandler()
    connection = db_connection_handler.get_engine().connect()

    products_repository = ProductRepository()
    products = products_repository.select_products()
    
    assert len(products) == 0
    assert products == []
    
    connection.close()
    
def test_select_products_by_ids():
    db_connection_handler = DBConnectionHandler()
    connection = db_connection_handler.get_engine().connect()

    products_id = [
        '016003a6-eeae-531c-b5bf-b537fd6348db',
        '0181680f-f5bf-5250-944d-2c3be9ae1082',
        '021c2220-5f60-5f05-b9d3-624dd05d3ff1',
        '04b01ac2-1200-5726-bb2e-d01cfab67159'
    ]
    
    products_repository = ProductRepository()   
    products = products_repository.select_products_by_ids(products_id)
    
    assert len(products) == products_id.__len__()
    for product in products:
        assert product.id in products_id
        assert product.name is not None
        assert product.stock is not None
        assert product.updated_at is not None
    connection.close()
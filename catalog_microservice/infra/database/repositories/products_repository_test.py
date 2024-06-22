import pytest
from sqlalchemy import text
from catalog_microservice.infra.database.settings.connection import DBConnectionHandler
from products_repository import ProductRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensive test")
def test_insert_product():
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
    products_repository = ProductRepository()
    products = products_repository.select_products()
    
    assert len(products) == 0
    assert products == []
    
    connection.close()
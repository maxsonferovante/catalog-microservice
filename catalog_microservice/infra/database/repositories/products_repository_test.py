import pytest
from sqlalchemy import text
from catalog_microservice.infra.database.settings.connection import DBConnectionHandler
from products_repository import ProductsRepository

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
    
    products_repository = ProductsRepository()
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
    
   
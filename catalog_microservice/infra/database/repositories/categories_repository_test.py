import pytest
from sqlalchemy import text
from catalog_microservice.infra.database.settings.connection import DBConnectionHandler
from categories_repository import CategoryRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensive test")
def test_insert_category():
    mocked_first_category = {
        "name": "Category 1",
        "description": "Description of category 1"
    }
    
    categories_repository = CategoryRepository()
    categories_repository.insert_category(
        name=mocked_first_category["name"],
        description=mocked_first_category["description"]
    )
    
    sql = '''
        SELECT * FROM categories 
        WHERE name = '{}' 
        AND description = '{}'
    '''.format(
        mocked_first_category["name"],
        mocked_first_category["description"]
    )
    
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    
    
    assert registry.name == mocked_first_category["name"]
    assert registry.description == mocked_first_category["description"]
    
    connection.execute(
        text(
            f'''
            DELETE FROM categories WHERE id = {registry.id}
            '''
        )
    )
    connection.commit()
    connection.close()
    
@pytest.mark.skip(reason="Sensive test")
def test_delete_category():
    mocked_first_category = {
        "name": "Category 1",
        "description": "Description of category 1"
    }
    
    categories_repository = CategoryRepository()
    categories_repository.insert_category(
        name=mocked_first_category["name"],
        description=mocked_first_category["description"]
    )
    
    sql = '''
        SELECT * FROM categories 
        WHERE name = '{}' 
        AND description = '{}'
    '''.format(
        mocked_first_category["name"],
        mocked_first_category["description"]
    )
    
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    
    categories_repository.delete_category(registry.id)
    
    sql = '''
        SELECT * FROM categories 
        WHERE name = '{}' 
        AND description = '{}'
    '''.format(
        mocked_first_category["name"],
        mocked_first_category["description"]
    )
    
    response = connection.execute(text(sql))
    registry = response.fetchall()
    
    assert len(registry) == 0
    
    connection.commit()
    connection.close()
    
    
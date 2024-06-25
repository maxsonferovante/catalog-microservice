from catalog_microservice.infra.database.tests.categories_repository import CategoryRepositorySpy

def test_insert_category():
    category_repository = CategoryRepositorySpy()
    category_repository.insert_category('category name', 'category description')
    assert category_repository.insert_category_atributes['name'] == 'category name'
    assert category_repository.insert_category_atributes['description'] == 'category description'
    
    
    
def test_register_category_with_invalid_name():
    category_repository = CategoryRepositorySpy()
    try:
        category_repository.insert_category(None, 'category description')
    except Exception as e:
        assert str(e) == 'Name must be a string'
        
    try:
        category_repository.insert_category(1, 'category description')
    except Exception as e:
        assert str(e) == 'Name must be a string'
        
def test_register_category_with_invalid_description():
    category_repository = CategoryRepositorySpy()
    try:
        category_repository.insert_category('category name', None)
    except Exception as e:
        assert str(e) == 'Description must be a string'
        
    try:
        category_repository.insert_category('category name', 1)
    except Exception as e:
        assert str(e) == 'Description must be a string'
        

import pytest
from connection import DBConnectionHandler

@pytest.mark.skip(reason="Sensitive data")
def test_create_database_engine():
    # Arrange
    db_connection_handler = DBConnectionHandler()
    
    # Act
    engine = db_connection_handler.get_engine()
    
    # Assert
    assert engine is not None
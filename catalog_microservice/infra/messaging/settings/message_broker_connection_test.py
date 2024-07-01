import pytest
from catalog_microservice.infra.messaging.settings.message_broker_connection import MessageBrokerConnectionHandler, MessageBrokerConnectionType

@pytest.mark.skip(reason="Sensive test")
def test_connection_producer():
    # Arrange
    connection_handler = MessageBrokerConnectionHandler(MessageBrokerConnectionType.PRODUCER)
    
    # Act
    broker = connection_handler.get_broker()
    
    # Assert
    assert broker is not None
    connection_handler.__exit__(None, None, None)

@pytest.mark.skip(reason="Sensive test")    
def test_connection_consumer():
    # Arrange
    connection_handler = MessageBrokerConnectionHandler(MessageBrokerConnectionType.CONSUMER)
    
    # Act
    broker = connection_handler.get_broker()
    
    # Assert
    assert broker is not None
    connection_handler.__exit__(None, None, None)

@pytest.mark.skip(reason="Sensive test")    
def test_invalid_connection_type():
    # Arrange
    try:
        connection_handler = MessageBrokerConnectionHandler(3)
    except ValueError as e:
        # Assert
        assert str(e) == "Invalid connection type. Use 'MessageBrokerConnectionType.PRODUCER' or 'MessageBrokerConnectionType.CONSUMER'"
    
    # Act
    
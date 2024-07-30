from cerberus import Validator
from catalog_microservice.errors.types.http_unprocessable_content import HttpUnprocessableContentError


def products_get_stock_validator(request: any):
    regex_uuid = '^[a-f0-9]{8}-[a-f0-9]{4}-5[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$'
    
    document_query = Validator({
        'products_ids': {
            'type': 'list',
            'required': True,
            'empty': False,
            'schema': {
                'type': 'string',
                'regex': regex_uuid
            }
        }
    })
    response = document_query.validate(request.json)
    
    if response is False:        
        raise HttpUnprocessableContentError(document_query.errors)
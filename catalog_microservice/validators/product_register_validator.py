from cerberus import Validator

from catalog_microservice.errors.types.http_unprocessable_content import HttpUnprocessableContentError

def product_register_validator(request: any):
    
    document_validator = Validator(
        {
         'name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 3, 'maxlength': 50},
         'description': {'type': 'string', 'required': True, 'empty': False, 'minlength': 3, 'maxlength': 255},
         'price': {'type': 'float', 'required': True, 'empty': False, 'min': 0.0},
         'category_id': {'type': 'integer', 'required': True, 'empty': False, 'min': 1}
        })
    
    
    response = document_validator.validate(request.json)
    if response is False:
            raise HttpUnprocessableContentError(document_validator.errors)
    
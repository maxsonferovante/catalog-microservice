from cerberus import Validator

from catalog_microservice.errors.types.http_unprocessable_content import HttpUnprocessableContentError

def product_register_validator(request: any):
    regex_uuid = '^[a-f0-9]{8}-[a-f0-9]{4}-5[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$'
    document_validator = Validator(
        {
         'name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 3, 'maxlength': 50},
         'description': {'type': 'string', 'required': True, 'empty': False, 'minlength': 3, 'maxlength': 255},
         'price': {'type': 'float', 'required': True, 'empty': False, 'min': 0.0},
         'stock': {'type': 'integer', 'required': True, 'empty': False, 'min': 0},
         'category_id': {'type': 'string', 'required': True, 'empty': False, 'regex': regex_uuid}
        })
    
    
    response = document_validator.validate(request.json)
    if response is False:
        for key, value in document_validator.errors.items():
            if value[0] == "value does not match regex '{}'".format(regex_uuid):           
                raise HttpUnprocessableContentError({key: 'The category_id must be an UUID string'})
        raise HttpUnprocessableContentError(document_validator.errors)
    
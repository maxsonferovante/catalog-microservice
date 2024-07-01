from cerberus import Validator

from catalog_microservice.errors.types.http_unprocessable_content import HttpUnprocessableContentError

def category_register_validator(request: any):    
    document_validator = Validator(
        {
         'name': 
             {'type': 'string', 'required': True, 'empty': False, 'minlength': 3, 'maxlength': 50},
         'description': 
             {'type': 'string', 'required': True, 'empty': False, 'minlength': 3, 'maxlength': 255}
        })
    response = document_validator.validate(request.json)
    if response is False:
            raise HttpUnprocessableContentError(document_validator.errors)
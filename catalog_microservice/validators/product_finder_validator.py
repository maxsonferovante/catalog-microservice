from cerberus import Validator
from catalog_microservice.errors.types.http_unprocessable_content import HttpUnprocessableContentError



def product_finder_validator(request: any):
    regex_uuid = '^[a-f0-9]{8}-[a-f0-9]{4}-5[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$'
        
    document_query = Validator({
            'product_id': {
                'type': 'string', 
                'required': True, 
                'empty': False, 
                'regex': regex_uuid,
                 }
            })
        
    response = document_query.validate(request.args)
    if response is False:
        for key, value in document_query.errors.items():
            print (key, value)
            if value[0] == "value does not match regex '{}'".format(regex_uuid):           
                raise HttpUnprocessableContentError({key: 'The product_id must be an UUID string'}) 
        raise HttpUnprocessableContentError(document_query.errors)
    



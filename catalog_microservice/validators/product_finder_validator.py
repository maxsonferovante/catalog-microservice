from cerberus import Validator


from catalog_microservice.errors.types.http_unprocessable_content import HttpUnprocessableContentError
def product_finder_validator(request: any):
    
    document_query = Validator({
            'product_id': {
                'type': 'string', 
                'required': True, 
                'empty': False, 
                'regex':  '^[1-9]+$',
                 }
            })
        
    response = document_query.validate(request.args)
    if response is False:
        # {'product_id': ["value does not match regex '^\\d+$'"]}
        for key, value in document_query.errors.items():
            print (key, value)
            if value[0] == "value does not match regex '^[1-9]+$'":           
                raise HttpUnprocessableContentError({key: 'The product_id must be an integer'})    
        raise HttpUnprocessableContentError(document_query.errors)
    



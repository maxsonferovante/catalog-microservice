from http import HTTPStatus
from catalog_microservice.presentation.http_types.http_response import HttpResponse
from catalog_microservice.errors.types.http_bad_request import HttpBadRequestError
from catalog_microservice.errors.types.http_unprocessable_content import HttpUnprocessableContentError
from catalog_microservice.errors.types.http_not_found import HttpNotFoundError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableContentError)):        
        return HttpResponse(status_code=error.status_code, body= {
            'errors': [
                {
                    'title':error.name,
                    'detail': error.message
                }
            ]            
        })    
    return HttpResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, body= {
            'errors': [
                {
                    'title': 'Server Error',
                    'detail': str(error)
                }
            ]
            
        })
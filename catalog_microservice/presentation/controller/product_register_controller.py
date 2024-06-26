from catalog_microservice.presentation.interface.controller_interface import ControllerInterface
from catalog_microservice.domain.use_cases.product_register_interface import ProductRegisterInterface

from catalog_microservice.presentation.http_types.http_request import HttpRequest
from catalog_microservice.presentation.http_types.http_response import HttpResponse

from http import HTTPStatus

class ProductRegisterController(ControllerInterface):
    
    def __init__(self, use_case: ProductRegisterInterface) -> None:
        self.__use_case = use_case
        
    def handle(self, http_request:  HttpRequest) -> HttpResponse:
        
        response = self.__use_case.register(
                http_request.body.get('name'),
                http_request.body.get('description'),
                http_request.body.get('price'),
                http_request.body.get('stock'),
                http_request.body.get('category_id')
            )
            
        return HttpResponse(
                status_code=HTTPStatus.CREATED,
                body={
                    'data': response
                }
            )
        
        
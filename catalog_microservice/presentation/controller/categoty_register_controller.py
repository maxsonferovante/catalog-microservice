from http import HTTPStatus

from catalog_microservice.presentation.http_types.http_request import HttpRequest
from catalog_microservice.presentation.http_types.http_response import HttpResponse

from catalog_microservice.presentation.interface.controller_interface import ControllerInterface
from catalog_microservice.domain.use_cases.category_register_interface import CategoryRegisterInterface


class CategoryRegisterController(ControllerInterface):
    def __init__(self, use_case: CategoryRegisterInterface) -> None:
            self.__use_case = use_case
            
    def handle(self, http_request:  HttpRequest) -> HttpResponse:
            
        response = self.__use_case.register(
                    http_request.body.get('name'),
                    http_request.body.get('description')
                )
                
        return HttpResponse(
                    status_code=HTTPStatus.CREATED,
                    body={
                        'data': response
                    }
                )

    
    
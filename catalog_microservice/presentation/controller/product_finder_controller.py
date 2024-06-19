from catalog_microservice.presentation.interface.controller_interface import ControllerInterface
from catalog_microservice.domain.use_cases.product_finder_interface import ProductFinderInterface

from catalog_microservice.presentation.http_types.http_request import HttpRequest
from catalog_microservice.presentation.http_types.http_response import HttpResponse

from http import HTTPStatus

class ProductFinderController(ControllerInterface):
    
    def __init__(self, use_case: ProductFinderInterface) -> None:
        self.__use_case = use_case
        
    def handle(self, http_request:  HttpRequest) -> HttpResponse:
        product_id = http_request.query_params.get('product_id')
        
        response = self.__use_case.find(product_id)
                
        return HttpResponse(
            status_code=HTTPStatus.OK,
            body={
                'data': response},
        )
        
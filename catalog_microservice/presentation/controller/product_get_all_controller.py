from catalog_microservice.presentation.interface.controller_interface import ControllerInterface
from catalog_microservice.domain.use_cases.product_get_all_interface import ProductGetAllInterface

from catalog_microservice.presentation.http_types.http_request import HttpRequest
from catalog_microservice.presentation.http_types.http_response import HttpResponse

from http import HTTPStatus

class ProductGetAllController(ControllerInterface):
    def __init__(self, use_case: ProductGetAllInterface) -> None:
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.use_case.get_all()
        
        return HttpResponse(
            status_code=HTTPStatus.OK,
            body={
                'data': response},
        )
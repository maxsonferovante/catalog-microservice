from catalog_microservice.presentation.interface.controller_interface import ControllerInterface
from catalog_microservice.domain.use_cases.product_get_stock_interface import ProductGetStockInterface

from catalog_microservice.presentation.http_types.http_request import HttpRequest
from catalog_microservice.presentation.http_types.http_response import HttpResponse

from http import HTTPStatus

class ProductGetStockController(ControllerInterface):
    
    def __init__(self, use_case: ProductGetStockInterface) -> None:
        self.use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        #  receberei uma lista de ids de produtos
        products_id = http_request.body['products_ids']
        
        response = self.use_case.get_stock(products_id)
        
        return HttpResponse(
            status_code=HTTPStatus.OK,
            body={
                'data': response},
        )
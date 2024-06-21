from typing import Callable
from flask import request as FlaskRequest
from catalog_microservice.presentation.http_types.http_request import HttpRequest
from catalog_microservice.presentation.http_types.http_response import HttpResponse

def request_adapter(request: FlaskRequest, controller: Callable) -> HttpResponse:
    
    body = None
    if request.data: body = request.json
    
    http_request = HttpRequest(
        query_params=request.args,
        path_params = request.view_args,
        body=body,
        headers=request.headers,
        method=request.method,
        url=request.full_path,
    )
    
    http_response = controller(http_request)
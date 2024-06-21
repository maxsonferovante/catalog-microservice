from flask import Blueprint, request, jsonify

from catalog_microservice.main.adapters.request_adapter import request_adapter

from catalog_microservice.main.composers.product_finder_composer import product_finder_composer
from catalog_microservice.main.composers.product_register_composer import product_register_composer


product_route_bp = Blueprint('product_routes', __name__)



@product_route_bp.route('/products/finder', methods=['GET'])
def finder_product():
    
    http_response = request_adapter(request=request, 
                                    controller=product_finder_composer()
                                    )
    return jsonify(http_response.body), http_response.status_code

@product_route_bp.route('/products/register', methods=['POST'])
def register_product():
    
    http_response = request_adapter(request=request, 
                                    controller=product_register_composer()
                                    )
    
    return jsonify(http_response.body), http_response.status_code
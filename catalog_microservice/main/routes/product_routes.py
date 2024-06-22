from flask import Blueprint, request, jsonify

from catalog_microservice.main.adapters.request_adapter import request_adapter

from catalog_microservice.main.composers.product_finder_composer import product_finder_composer
from catalog_microservice.main.composers.product_register_composer import product_register_composer
from catalog_microservice.main.composers.product_get_all_composer import product_get_all_composer

from catalog_microservice.errors.error_handler import handle_errors
from catalog_microservice.validators.product_register_validator import product_register_validator

product_route_bp = Blueprint('product_routes', __name__)



@product_route_bp.route('/products/finder', methods=['GET'])
def finder_product():
    http_response = None
    
    try:
        http_response = request_adapter(request=request, controller=product_finder_composer())
    except Exception as error:
        http_response = handle_errors(error)
    
    return jsonify(http_response.body), http_response.status_code

@product_route_bp.route('/products/register', methods=['POST'])
def register_product():
    
    http_response = None
    try:
        product_register_validator(request)
        http_response = request_adapter(request=request, controller=product_register_composer())
    except Exception as error:
        http_response = handle_errors(error)
    
    return jsonify(http_response.body), http_response.status_code


@product_route_bp.route('/products/all', methods=['GET'])
def get_all_products():
    http_response = None
    
    try:
        http_response = request_adapter(request=request, controller=product_get_all_composer())
    except Exception as error:
        http_response = handle_errors(error)
    
    return jsonify(http_response.body), http_response.status_code
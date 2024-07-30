from flask import Blueprint, request, jsonify

from catalog_microservice.main.adapters.request_adapter import request_adapter

from catalog_microservice.main.composers.product_finder_composer import product_finder_composer
from catalog_microservice.main.composers.product_register_composer import product_register_composer
from catalog_microservice.main.composers.product_get_all_composer import product_get_all_composer
from catalog_microservice.main.composers.product_get_stock_composer import product_get_stock_composer

from catalog_microservice.errors.error_handler import handle_errors
from catalog_microservice.validators.product_register_validator import product_register_validator
from catalog_microservice.validators.product_finder_validator import product_finder_validator
from catalog_microservice.validators.products_get_stock import products_get_stock_validator

product_route_bp = Blueprint('product_routes', __name__)



@product_route_bp.route('/products/finder', methods=['GET'])
def finder_product():
    http_response = None
    
    try:
        product_finder_validator(request=request)
        http_response = request_adapter(request=request, controller=product_finder_composer())
    except Exception as error:
        http_response = handle_errors(error)
    
    return jsonify(http_response.body), http_response.status_code

@product_route_bp.route('/products/register', methods=['POST'])
def register_product():
    
    http_response = None
    try:
        product_register_validator(request=request)
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


@product_route_bp.route('/products/stock', methods=['POST'])
def get_stock():
    http_response = None
    
    try:
        products_get_stock_validator(request=request)
        http_response = request_adapter(request=request, controller=product_get_stock_composer())
    except Exception as error:
        http_response = handle_errors(error)
    
    return jsonify(http_response.body), http_response.status_code


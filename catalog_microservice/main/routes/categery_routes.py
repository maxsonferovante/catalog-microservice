from flask import Blueprint, request, jsonify

from catalog_microservice.main.adapters.request_adapter import request_adapter

from catalog_microservice.main.composers.category_register_composer import category_register_composer

from catalog_microservice.errors.error_handler import handle_errors

from catalog_microservice.validators.category_register_validator import category_register_validator


category_route_bp = Blueprint('category_routes', __name__)


@category_route_bp.route('/categories/register', methods=['POST'])
def register_category():
    
    http_response = None
    try:
        category_register_validator(request=request)
        http_response = request_adapter(request=request, controller=category_register_composer())
    except Exception as error:
        http_response = handle_errors(error)
    
    return jsonify(http_response.body), http_response.status_code
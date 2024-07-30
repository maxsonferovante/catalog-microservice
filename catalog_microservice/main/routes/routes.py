from flask import Blueprint, request, jsonify
from http import HTTPStatus
""" 
criar uma rota metodo get para apresentar a api 
"""

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def home():
    return jsonify(
        {
            'message': 'API Catalog Microservice',
            'author': 'Maxson Almeida',
            'version': '0.1.1',
        }), HTTPStatus.OK
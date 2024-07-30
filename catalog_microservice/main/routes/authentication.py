from http import HTTPStatus

from flask import Blueprint, request, jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from catalog_microservice.infra.utils.generate_uuid import generate_uuid

authentication_bp = Blueprint('authentication_routes', __name__)


@authentication_bp.route('/authentication/token', methods=['POST'])
def authentication_token():
    uuid_user = generate_uuid()    
    
    access_token = create_access_token(identity=uuid_user, fresh=True)
    
    refresh_token = create_refresh_token(identity=uuid_user)
    
   
    return jsonify(        
        data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user_identity': uuid_user,
            'message': 'User authenticated'
        }
    ), HTTPStatus.OK
    
@authentication_bp.route('/authentication/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user, fresh=False)
    return jsonify(access_token=access_token), HTTPStatus.OK
    

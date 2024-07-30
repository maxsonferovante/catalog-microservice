import os
from datetime import timedelta
from flask import Flask
from flask_cors import CORS

from flask_jwt_extended import JWTManager

from catalog_microservice.main.routes.authentication import authentication_bp
from catalog_microservice.main.routes.routes import home_bp
from catalog_microservice.main.routes.product_routes import product_route_bp
from catalog_microservice.main.routes.categery_routes import category_route_bp

from catalog_microservice.infra.utils.generate_uuid import generate_uuid

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] =  os.environ.get('JWT_SECRET_KEY', generate_uuid())
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)

CORS(app)

app.register_blueprint(authentication_bp)
app.register_blueprint(home_bp)
app.register_blueprint(product_route_bp)
app.register_blueprint(category_route_bp)


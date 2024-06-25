from flask import Flask
from flask_cors import CORS

from catalog_microservice.main.routes.product_routes import product_route_bp
from catalog_microservice.main.routes.categery_routes import category_route_bp
from catalog_microservice.main.routes.routes import home_bp

app = Flask(__name__)


CORS(app)


app.register_blueprint(home_bp)
app.register_blueprint(product_route_bp)
app.register_blueprint(category_route_bp)


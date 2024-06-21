from flask import Flask

from catalog_microservice.main.routes.product_routes import product_route_bp
from catalog_microservice.main.routes.routes import home_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(product_route_bp)

from catalog_microservice.main.server.server import app


def run():
    app.run(debug=True,
            host='0.0.0.0',
            port=5000,
            load_dotenv=True)
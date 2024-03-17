from .controller import indexRoutes
from .controller.employeesController import employee_routes_blueprint
from flask import Flask
from flask_cors import CORS
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "False"}})

def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(indexRoutes.main, url_prefix='/')
    app.register_blueprint(employee_routes_blueprint, url_prefix='/employees')


    return app

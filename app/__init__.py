from flask import Flask
from flask_bootstrap import Bootstrap

from instance.config import config_options


bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__, instance_relative_config= True)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config.from_pyfile('config.py')
    config_options[config_name].init_app(app)
    
    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import config_request
    config_request(app)

    return app
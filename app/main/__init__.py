from flask import Flask , Blueprint
from flask_bootstrap import Bootstrap
from .config import DevConfig
from . import views, error

# Initializing application
app = Flask(__name__,instance_relative_config = True)

  # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app

from app import views
from app import error

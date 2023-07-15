from flask import Flask
from .models import db
from pokemon_battle.api import api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/openapi.json'  # API url (local resource)

def create_app(settings_overrides=None):
    app = Flask(__name__)
    CORS(app)
    configure_settings(app, settings_overrides)

    # Initialize the database
    db.init_app(app)

    # Create the necessary tables
    with app.app_context():
        db.create_all()
    
    configure_blueprints(app)
    return app


def configure_settings(app, settings_override):
    app.config.update({
        'DEBUG': True,
        'TESTING': False,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///pokemon_battle.sqlite'
    })
    if settings_override:
        app.config.update(settings_override)


def configure_blueprints(app):
    app.register_blueprint(api)

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, 
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Pokemon Battlefield"
        },
    )
    app.register_blueprint(swaggerui_blueprint)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)  # Enable CORS for the app    
    db.init_app(app)  # Initialize SQLAlchemy with the app
    jwt.init_app(app)  # Initialize JWTManager with the app

    # Route imports and registration
    from .routes.employees import employees_bp
    from auth.login import login_bp
    app.register_blueprint(employees_bp, url_prefix='/api/employees')
    app.register_blueprint(login_bp, url_prefix='/api/auth')

    return app
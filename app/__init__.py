from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from app.models import db


jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # extensions
    CORS(app)
    db.init_app(app)
    jwt.init_app(app)

    # blueprints 
    from app.routes.employees import employee_bp
    from auth.login import auth_bp
    from app.routes.documents import documents_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(employee_bp, url_prefix="/api/employees")
    app.register_blueprint(documents_bp, url_prefix="/api")

    return app

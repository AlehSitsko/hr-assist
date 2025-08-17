from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.models import db
import os

def create_app():
    app = Flask(__name__)

    # base configuration 
    app.config.setdefault("SECRET_KEY", os.getenv("SECRET_KEY", "dev-secret"))
    app.config.setdefault("JWT_SECRET_KEY", os.getenv("JWT_SECRET_KEY", "dev-jwt"))
    app.config.setdefault("SQLALCHEMY_DATABASE_URI", os.getenv("DATABASE_URL", "sqlite:///app.db"))
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    app.config.setdefault("UPLOAD_FOLDER", os.getenv("UPLOAD_FOLDER", "uploads"))
    app.config.setdefault("MAX_CONTENT_LENGTH", 10 * 1024 * 1024)  # 10MB
    app.config.setdefault("TESTING", False)

    # for sqlite :memory: in tests (single connection)
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite:///:memory:"):
        from sqlalchemy.pool import StaticPool
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
            "poolclass": StaticPool,
            "connect_args": {"check_same_thread": False},
        }

    db.init_app(app)
    JWTManager(app)
    CORS(app)  # in production, fix origins

    # Blueprints
    from app.routes.employees import employee_bp
    from app.routes.documents import documents_bp
    from auth.login import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(employee_bp, url_prefix="/api/employees")
    app.register_blueprint(documents_bp, url_prefix="/api")

    # 413 handler
    @app.errorhandler(413)
    def too_large(_):
        return {"error": "File too large"}, 413

    return app

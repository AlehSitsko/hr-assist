import os
import pytest
from app import create_app
from app.models import db

# ENV для тестов
os.environ.setdefault("SECRET_KEY", "test")
os.environ.setdefault("JWT_SECRET_KEY", "testjwt")
os.environ.setdefault("ADMIN_USERNAME", "admin")
os.environ.setdefault("ADMIN_PASSWORD", "1234")
# надёжнее файл, чем :memory:
os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")

@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def token(client):
    r = client.post("/api/auth/login", json={"username":"admin","password":"1234"})
    assert r.status_code == 200
    return r.get_json()["access_token"]

# Чистим БД перед каждым тестом
@pytest.fixture(autouse=True)
def _db_reset(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
    yield

def auth_hdr(tok): 
    return {"Authorization": f"Bearer {tok}"}

# tests/test_api.py
import os
import pytest
from datetime import timedelta

os.environ.setdefault("SECRET_KEY", "test")
os.environ.setdefault("JWT_SECRET_KEY", "testjwt")
os.environ.setdefault("ADMIN_USERNAME", "admin")
os.environ.setdefault("ADMIN_PASSWORD", "1234")
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")

from app import create_app
from app.models import db

@pytest.fixture(scope="session")
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def token(client):
    resp = client.post("/api/auth/login", json={"username": "admin", "password": "1234"})
    assert resp.status_code == 200, resp.text
    return resp.get_json()["access_token"]

def auth_hdr(token): 
    return {"Authorization": f"Bearer {token}"}

def test_login_ok(client):
    r = client.post("/api/auth/login", json={"username":"admin","password":"1234"})
    assert r.status_code == 200 and "access_token" in r.get_json()

def test_login_bad(client):
    r = client.post("/api/auth/login", json={"username":"admin","password":"wrong"})
    assert r.status_code == 401

@pytest.mark.xfail(reason="GET / bound to delete_employee by stray decorator")
def test_employees_get_broken_route(client, token):
    r = client.get("/api/employees/", headers=auth_hdr(token))
    assert r.status_code == 200  # ожидаемый таргет после фикса

def test_employees_delete_unauth(client):
    r = client.delete("/api/employees/1")
    assert r.status_code in (401, 422)  # без токена

def test_employees_delete_not_found(client, token):
    r = client.delete("/api/employees/9999", headers=auth_hdr(token))
    assert r.status_code == 404

@pytest.mark.xfail(reason="upload endpoint unfinished (ellipsis)")
def test_upload_document_unfinished(client, token):
    import io
    data = {"file": (io.BytesIO(b"%PDF-1.4\n%..."), "test.pdf")}
    r = client.post("/api/employees/1/documents", headers=auth_hdr(token), data=data, content_type="multipart/form-data")
    assert r.status_code == 201  # целевое поведение после реализации

def test_utils_allowed_file():
    from app.utils import allowed_file
    assert allowed_file("a.pdf")
    assert allowed_file("b.JPG")
    assert not allowed_file("")
    assert not allowed_file("noext")

import io
import os
from app.models import db, Employee


def ensure_emp(app, emp_id=777):
    """Создать тестового сотрудника, если его нет"""
    with app.app_context():
        if not db.session.get(Employee, emp_id):
            db.session.add(
                Employee(
                    id=emp_id,
                    first_name="Doc",
                    last_name="Holder",
                    email=f"doc{emp_id}@ex.com",
                    certification="EMT-B",
                )
            )
            db.session.commit()


def test_upload_document_pdf(app, client, token, tmp_path):
    ensure_emp(app, 777)
    app.config["UPLOAD_FOLDER"] = str(tmp_path)

    data = {"file": (io.BytesIO(b"%PDF-1.4\n%..."), "test.pdf")}
    r = client.post(
        "/api/employees/777/documents",
        headers={"Authorization": f"Bearer {token}"},
        data=data,
        content_type="multipart/form-data",
    )
    assert r.status_code == 201
    body = r.get_json()
    assert body["employee_id"] == 777
    assert body["original_name"] == "test.pdf"
    # файл действительно записался
    assert os.path.exists(tmp_path / body["stored_name"])


def test_upload_document_no_file(app, client, token, tmp_path):
    ensure_emp(app, 778)
    app.config["UPLOAD_FOLDER"] = str(tmp_path)

    r = client.post(
        "/api/employees/778/documents",
        headers={"Authorization": f"Bearer {token}"},
        data={},
        content_type="multipart/form-data",
    )
    assert r.status_code == 400


def test_upload_document_bad_ext(app, client, token, tmp_path):
    ensure_emp(app, 779)
    app.config["UPLOAD_FOLDER"] = str(tmp_path)

    data = {"file": (io.BytesIO(b"hello"), "evil.exe")}
    r = client.post(
        "/api/employees/779/documents",
        headers={"Authorization": f"Bearer {token}"},
        data=data,
        content_type="multipart/form-data",
    )
    assert r.status_code == 400


def test_upload_document_emp_not_found(client, token, tmp_path, app):
    app.config["UPLOAD_FOLDER"] = str(tmp_path)
    data = {"file": (io.BytesIO(b"%PDF-1.4"), "x.pdf")}
    r = client.post(
        "/api/employees/99999/documents",
        headers={"Authorization": f"Bearer {token}"},
        data=data,
        content_type="multipart/form-data",
    )
    assert r.status_code == 404


def test_upload_same_original_name_gets_unique_store_names(app, client, token, tmp_path):
    """Если дважды загрузить один и тот же файл с одинаковым именем —
    должны получиться разные stored_name
    """
    with app.app_context():
        emp = Employee(
            id=880,
            first_name="Doc",
            last_name="Dup",
            email="dup@example.com",
            certification="EMT-B",
        )
        db.session.add(emp)
        db.session.commit()

    app.config["UPLOAD_FOLDER"] = str(tmp_path)

    # первый аплоад
    data1 = {"file": (io.BytesIO(b"%PDF-1.4\n%..."), "dup.pdf")}
    r1 = client.post(
        "/api/employees/880/documents",
        headers={"Authorization": f"Bearer {token}"},
        data=data1,
        content_type="multipart/form-data",
    )
    assert r1.status_code == 201
    s1 = r1.get_json()["stored_name"]

    # второй аплоад (новый BytesIO!)
    data2 = {"file": (io.BytesIO(b"%PDF-1.4\n%..."), "dup.pdf")}
    r2 = client.post(
        "/api/employees/880/documents",
        headers={"Authorization": f"Bearer {token}"},
        data=data2,
        content_type="multipart/form-data",
    )
    assert r2.status_code == 201
    s2 = r2.get_json()["stored_name"]

    assert s1 != s2

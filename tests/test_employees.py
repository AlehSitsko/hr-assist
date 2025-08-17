EMP = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "position": "EMT",
    "certification": "EMT-B",
    "certification_expiration": "2030-01-01",
    "is_active": True,
    "cpr_certified": True,
    "cpr_expiration": "2030-01-01",
    "is_cpr_active": True,
    "evoc_certified": False,
    "evoc_expiration": "2030-01-01",
    "is_evoc_active": False,
    "dl_number": "A1234567",
    "dl_expiration": "2030-01-01",
    "is_dl_active": True,
    "phone": "555-0000",
    "address": "1 Main St",
    "date_of_birth": "1990-02-03",
    "start_date": "2020-04-05",
    "created_by": "tests",
    "notes": "ok"
}

def H(tok): return {"Authorization": f"Bearer {tok}"}

def test_employees_empty_list(client, token):
    r = client.get("/api/employees/", headers=H(token))
    assert r.status_code == 200 and r.get_json() == []

def test_create_employee(client, token):
    r = client.post("/api/employees/", headers=H(token), json=EMP)
    assert r.status_code == 201
    emp_id = r.get_json()["id"]

    r = client.get(f"/api/employees/{emp_id}", headers=H(token))
    assert r.status_code == 200
    body = r.get_json()
    assert body["email"] == EMP["email"]
    assert body["first_name"] == "John"

def test_create_dupe_email(client, token):
    r1 = client.post("/api/employees/", headers=H(token), json=EMP)
    assert r1.status_code == 201
    r2 = client.post("/api/employees/", headers=H(token), json=EMP)
    assert r2.status_code == 409

def test_update_employee_email_conflict(client, token):
    client.post("/api/employees/", headers=H(token), json=EMP)
    r = client.post("/api/employees/", headers=H(token), json={**EMP, "email": "other@example.com"})
    emp2 = r.get_json()["id"]

    r = client.put(f"/api/employees/{emp2}", headers=H(token), json={"email": "john@example.com"})
    assert r.status_code == 409

def test_update_employee_ok(client, token):
    r = client.post("/api/employees/", headers=H(token), json=EMP)
    emp_id = r.get_json()["id"]

    r = client.put(f"/api/employees/{emp_id}", headers=H(token), json={
        "phone": "555-1111",
        "cpr_expiration": "2031-01-01"
    })
    assert r.status_code == 200

    r = client.get(f"/api/employees/{emp_id}", headers=H(token))
    body = r.get_json()
    assert body["phone"] == "555-1111"
    assert body["cpr_expiration"].startswith("2031-01-01")

def test_delete_employee(client, token):
    r = client.post("/api/employees/", headers=H(token), json={**EMP, "email": "todel@example.com"})
    emp_id = r.get_json()["id"]

    r = client.delete(f"/api/employees/{emp_id}", headers=H(token))
    assert r.status_code == 200

    r = client.get(f"/api/employees/{emp_id}", headers=H(token))
    assert r.status_code == 404

def test_login_ok(client):
    r = client.post("/api/auth/login", json={"username":"admin","password":"1234"})
    assert r.status_code == 200 and "access_token" in r.get_json()

def test_login_bad(client):
    r = client.post("/api/auth/login", json={"username":"admin","password":"nope"})
    assert r.status_code == 401

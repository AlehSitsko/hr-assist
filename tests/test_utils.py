import pytest
from datetime import date, timedelta, datetime
from app.utils import allowed_file, secure_store_name, cert_status
from config import EXPIRY_SOON_DAYS

def test_allowed_file():
    assert allowed_file("a.pdf")
    assert allowed_file("b.JPG")
    assert not allowed_file("noext")
    assert not allowed_file("")
    assert not allowed_file(None)

def test_secure_store_name():
    n1 = secure_store_name("My File.PDF")
    n2 = secure_store_name("My File.PDF")
    assert n1.lower().endswith(".pdf")
    assert n1 != n2

def test_secure_store_name_invalid():
    with pytest.raises(ValueError):
        secure_store_name("")
    with pytest.raises(ValueError):
        secure_store_name("   ")

def test_cert_status_states():
    today = date.today()
    assert cert_status(None) == "N/A"
    assert cert_status(today - timedelta(days=1)) == "Expired"
    assert cert_status(today) == "Expiring Soon"
    assert cert_status(today + timedelta(days=EXPIRY_SOON_DAYS)) == "Expiring Soon"
    assert cert_status(today + timedelta(days=EXPIRY_SOON_DAYS + 1)) == "Active"

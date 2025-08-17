# --- File helpers ---
import uuid
from werkzeug.utils import secure_filename
from config import ALLOWED_EXTENSIONS  

def allowed_file(filename: str) -> bool:
    if not filename:
        return False
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def unique_filename(original: str) -> str:
    ext = original.rsplit(".", 1)[1].lower() if "." in original else ""
    return f"{uuid.uuid4().hex}.{ext}" if ext else uuid.uuid4().hex

def secure_store_name(filename: str) -> str:
    cleaned = secure_filename(filename or "")
    if not cleaned:
        raise ValueError("Invalid filename")
    return unique_filename(cleaned)

# --- Certificate helpers ---
from datetime import date, datetime, timedelta
from config import EXPIRY_SOON_DAYS

def cert_status(expires_on) -> str:
    if not expires_on:
        return "N/A"
    if isinstance(expires_on, datetime):
        expires_on = expires_on.date()
    today = date.today()
    if expires_on < today:
        return "Expired"
    if expires_on <= today + timedelta(days=EXPIRY_SOON_DAYS):
        return "Expiring Soon"
    return "Active"

def employee_cert_summary(emp):
    return {
        "CPR":  cert_status(getattr(emp, "cpr_expiration", None)),
        "EVOC": cert_status(getattr(emp, "evoc_expiration", None)),
        "DL":   cert_status(getattr(emp, "dl_expiration", None)),
    }

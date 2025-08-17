from flask import Blueprint, jsonify, request
from datetime import datetime, date
from flask_jwt_extended import jwt_required
from app.models import db, Employee

employee_bp = Blueprint("employee", __name__)

DATE_FMT = "%Y-%m-%d"

DATE_FIELDS = {
    "certification_expiration",
    "cpr_expiration",
    "evoc_expiration",
    "dl_expiration",
    "date_of_birth",
    "start_date",
    "updated_at",
    "created_at",
}

UPDATABLE_FIELDS = {
    "first_name", "last_name", "position",
    "certification", "certification_expiration",
    "is_active",
    "cpr_certified", "cpr_expiration", "is_cpr_active",
    "evoc_certified", "evoc_expiration", "is_evoc_active",
    "dl_number", "dl_expiration", "is_dl_active",
    "email", "phone", "address",
    "date_of_birth", "start_date",
    "notes",
    # "documents",
}

REQUIRED_ON_CREATE = {"first_name", "last_name", "email", "certification"}

def parse_date_or_none(value):
    if not value:
        return None
    if isinstance(value, (datetime, date)):
        return value if isinstance(value, date) else value.date()
    return datetime.strptime(value, DATE_FMT).date()

def to_iso(val):
    if isinstance(val, (datetime, date)):
        return val.isoformat()
    return val

def serialize_employee(emp: Employee) -> dict:
    out = {c.name: getattr(emp, c.name) for c in emp.__table__.columns}
    for k, v in out.items():
        out[k] = to_iso(v)
    return out

@employee_bp.get("/")
@jwt_required()
def get_employees():
    employees = db.session.execute(db.select(Employee)).scalars().all()
    return jsonify([serialize_employee(e) for e in employees]), 200

@employee_bp.get("/<int:id>")
@jwt_required()
def get_employee(id: int):
    emp = db.session.get(Employee, id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(serialize_employee(emp)), 200

@employee_bp.post("/")
@jwt_required()
def create_employee():
    data = request.get_json(silent=True) or {}
    missing = [f for f in REQUIRED_ON_CREATE if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    # уникальность email
    exists = db.session.execute(db.select(Employee).filter_by(email=data["email"])).scalar_one_or_none()
    if exists:
        return jsonify({"error": "Email already exists"}), 409

    try:
        emp = Employee(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            position=data.get("position"),
            certification=data.get("certification"),
            certification_expiration=parse_date_or_none(data.get("certification_expiration")),
            is_active=bool(data.get("is_active", True)),

            cpr_certified=bool(data.get("cpr_certified", False)),
            cpr_expiration=parse_date_or_none(data.get("cpr_expiration")),
            is_cpr_active=bool(data.get("is_cpr_active", False)),

            evoc_certified=bool(data.get("evoc_certified", False)),
            evoc_expiration=parse_date_or_none(data.get("evoc_expiration")),
            is_evoc_active=bool(data.get("is_evoc_active", False)),

            dl_number=data.get("dl_number"),
            dl_expiration=parse_date_or_none(data.get("dl_expiration")),
            is_dl_active=bool(data.get("is_dl_active", False)),

            email=data.get("email"),
            phone=data.get("phone"),
            address=data.get("address"),
            date_of_birth=parse_date_or_none(data.get("date_of_birth")),
            start_date=parse_date_or_none(data.get("start_date")),
            created_by=data.get("created_by"),
            notes=data.get("notes"),
            # documents=data.get("documents"),
        )
        db.session.add(emp)
        db.session.commit()
        return jsonify({"message": "Employee created", "id": emp.id}), 201
    except ValueError as ve:
        return jsonify({"error": f"Invalid data: {ve}"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@employee_bp.put("/<int:id>")
@jwt_required()
def update_employee(id: int):
    data = request.get_json(silent=True) or {}
    emp = db.session.get(Employee, id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    # уникальность email при апдейте
    if "email" in data and data["email"] != emp.email:
        exists = db.session.execute(
            db.select(Employee).filter(Employee.email == data["email"], Employee.id != id)
        ).scalar_one_or_none()
        if exists:
            return jsonify({"error": "Email already exists"}), 409

    try:
        for key, value in data.items():
            if key not in UPDATABLE_FIELDS:
                continue
            if key in DATE_FIELDS:
                value = parse_date_or_none(value)
            setattr(emp, key, value)

        emp.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": "Employee updated"}), 200
    except ValueError as ve:
        return jsonify({"error": f"Invalid data: {ve}"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@employee_bp.delete("/<int:id>")
@jwt_required()
def delete_employee(id: int):
    emp = db.session.get(Employee, id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    try:
        db.session.delete(emp)
        db.session.commit()
        return jsonify({"message": "Employee deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

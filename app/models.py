from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name  = db.Column(db.String(100), nullable=False)

    # may not be specified
    position = db.Column(db.String(100), nullable=True)

    # Required certifications
    certification = db.Column(db.String(100), nullable=False)
    certification_expiration = db.Column(db.Date, nullable=True)

    is_active = db.Column(db.Boolean, default=True)

    cpr_certified   = db.Column(db.Boolean, default=False)
    cpr_expiration  = db.Column(db.Date, nullable=True)
    is_cpr_active   = db.Column(db.Boolean, default=False)

    evoc_certified  = db.Column(db.Boolean, default=False)
    evoc_expiration = db.Column(db.Date, nullable=True)
    is_evoc_active  = db.Column(db.Boolean, default=False)

    dl_number    = db.Column(db.String(20), nullable=True)
    dl_expiration = db.Column(db.Date, nullable=True)
    is_dl_active  = db.Column(db.Boolean, default=False)

    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(200), nullable=True)

    date_of_birth = db.Column(db.Date, nullable=True)
    date_joined   = db.Column(db.DateTime, default=datetime.utcnow)

    notes = db.Column(db.Text, nullable=True)

    # Placeholder for document paths, can be removed later
    documents = db.Column(db.String(200), nullable=True)

    start_date = db.Column(db.Date, nullable=True)

    created_by = db.Column(db.String(100), nullable=True, default="system")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    updated_by = db.Column(db.String(100), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    files = db.relationship(
        "Document",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Employee {self.first_name} {self.last_name}>"

class Document(db.Model):
    __tablename__ = "documents"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)

    stored_name   = db.Column(db.String(255), nullable=False)
    original_name = db.Column(db.String(255), nullable=False)
    mimetype      = db.Column(db.String(100))
    size_bytes    = db.Column(db.Integer)
    uploaded_at   = db.Column(db.DateTime, default=datetime.utcnow)

    employee = db.relationship("Employee", back_populates="files")

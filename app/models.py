from . import db
from datetime import datetime

# Employee model for the HR management system
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for each employee
    first_name = db.Column(db.String(100), nullable=False) # First name of the employee
    last_name = db.Column(db.String(100), nullable=False) # Last name of the employee
    position = db.Column(db.String(100), nullable=False) # Position of the employee
    certification = db.Column(db.String(100), nullable=False) # Certification held by the employee
    certification_expiration = db.Column(db.Date, nullable=False) # Expiration date of the certification
    is_active = db.Column(db.Boolean, default=True) # Employment status
    cpr_certified = db.Column(db.Boolean, default=False) # CPR certification status
    cpr_expiration = db.Column(db.Date, nullable=False) # Expiration date of CPR certification
    is_cpr_active = db.Column(db.Boolean, default=False) # CPR certification active status
    evoc_certified = db.Column(db.Boolean, default=False) # EVOC certification status
    evoc_expiration = db.Column(db.Date, nullable=False) # Expiration date of EVOC certification
    is_evoc_active = db.Column(db.Boolean, default=False) # EVOC certification active status
    dl_number = db.Column(db.String(20), nullable=False) # Driver's license number
    dl_expiration = db.Column(db.Date, nullable=False) # Expiration date of driver's license
    is_dl_active = db.Column(db.Boolean, default=False) # Driver's license active status
    email = db.Column(db.String(120), unique=True, nullable=False) # Email address
    phone = db.Column(db.String(20), nullable=False) # Phone number
    address = db.Column(db.String(200), nullable=False) # Home address
    date_of_birth = db.Column(db.Date, nullable=False) # Date of birth
    date_joined = db.Column(db.DateTime, default=datetime.utcnow) # Date when the employee joined
    notes = db.Column(db.Text, nullable=True)   # Additional notes about the employee
    documents = db.Column(db.String(200), nullable=True)  # Path to uploaded documents/Relation
    start_date = db.Column(db.Date, nullable=False) # Start date of employment
    created_by = db.Column(db.String(100), nullable=False) # User who created the employee record
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # Timestamp of record creation
    updated_by = db.Column(db.String(100), nullable=True) # User who last updated the employee record
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) # Timestamp of the last update


    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'
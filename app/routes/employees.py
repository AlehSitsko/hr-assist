from flask import Blueprint, jsonify, request
from app import db
from app.models import Employee
from datetime import datetime
from flask_jwt_extended import jwt_required

employee_bp = Blueprint('employee', __name__)

# Helper to convert employee to dict

def serialize_employee(employee):
    return {column.name: getattr(employee, column.name) for column in employee.__table__.columns}


# Get all employees
@employee_bp.route('/', methods=['GET'])
@jwt_required()
def get_employees():
    employees = Employee.query.all()
    return jsonify([serialize_employee(e) for e in employees]), 200


# Get single employee by ID
@employee_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(serialize_employee(employee)), 200


# Create new employee
@employee_bp.route('/', methods=['POST'])
@jwt_required()
def create_employee():
    data = request.json
    if Employee.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 409
    try:
        new_employee = Employee(
            first_name=data['first_name'],
            last_name=data['last_name'],
            position=data['position'],
            certification=data['certification'],
            certification_expiration=datetime.strptime(data['certification_expiration'], '%Y-%m-%d'),
            is_active=data.get('is_active', True),
            cpr_certified=data.get('cpr_certified', False),
            cpr_expiration=datetime.strptime(data['cpr_expiration'], '%Y-%m-%d'),
            is_cpr_active=data.get('is_cpr_active', False),
            evoc_certified=data.get('evoc_certified', False),
            evoc_expiration=datetime.strptime(data['evoc_expiration'], '%Y-%m-%d'),
            is_evoc_active=data.get('is_evoc_active', False),
            dl_number=data['dl_number'],
            dl_expiration=datetime.strptime(data['dl_expiration'], '%Y-%m-%d'),
            is_dl_active=data.get('is_dl_active', False),
            email=data['email'],
            phone=data['phone'],
            address=data['address'],
            date_of_birth=datetime.strptime(data['date_of_birth'], '%Y-%m-%d'),
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            created_by=data['created_by'],
            notes=data.get('notes'),
            documents=data.get('documents')
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({"message": "Employee created", "id": new_employee.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Update existing employee
@employee_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_employee(id):
    data = request.json
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    try:
        for key, value in data.items():
            if hasattr(employee, key):
                if 'date' in key or 'expiration' in key:
                    setattr(employee, key, datetime.strptime(value, '%Y-%m-%d'))
                else:
                    setattr(employee, key, value)
        employee.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": "Employee updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete employee
@employee_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    try:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({"message": "Employee deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

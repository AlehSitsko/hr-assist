# app/routes/documents.py
import os
from flask import Blueprint, request, jsonify, current_app, send_from_directory
from flask_jwt_extended import jwt_required
from app.models import db, Employee, Document
from config import UPLOAD_FOLDER
from app.utils import allowed_file, secure_store_name

documents_bp = Blueprint("documents", __name__)

@documents_bp.post("/employees/<int:emp_id>/documents")
@jwt_required()
def upload_document(emp_id):
    emp = Employee.query.get_or_404(emp_id)

    if "file" not in request.files:
        return {"error": "No file part"}, 400
    f = request.files["file"]
    if not f or f.filename == "":
        return {"error": "No selected file"}, 400
    if not allowed_file(f.filename):
        return {"error": "File type not allowed"}, 400

    stored = secure_store_name(f.filename)
    full_path = os.path.join(UPLOAD_FOLDER, stored)
    f.save(full_path)

    doc = Document(
        employee_id=emp.id,
        stored_name=stored,
        original_name=f.filename,
        mimetype=f.mimetype,
        size_bytes=os.path.getsize(full_path),
    )
    db.session.add(doc)
    db.session.commit()

    return {
        "id": doc.id,
        "original_name": doc.original_name,
        "uploaded_at": doc.uploaded_at.isoformat()
    }, 201

@documents_bp.get("/employees/<int:emp_id>/documents")
@jwt_required()
def list_documents(emp_id):
    Employee.query.get_or_404(emp_id)  # 404 если нет
    docs = (Document.query
            .filter_by(employee_id=emp_id)
            .order_by(Document.uploaded_at.desc())
            .all())
    return jsonify([
        {
            "id": d.id,
            "original_name": d.original_name,
            "mimetype": d.mimetype,
            "size_bytes": d.size_bytes,
            "uploaded_at": d.uploaded_at.isoformat(),
        } for d in docs
    ])

@documents_bp.get("/documents/<int:doc_id>/download")
@jwt_required()
def download_document(doc_id):
    d = Document.query.get_or_404(doc_id)
    return send_from_directory(
        directory=UPLOAD_FOLDER,
        path=d.stored_name,         # Flask 3: аргумент называется path
        as_attachment=True,
        download_name=d.original_name
    )

@documents_bp.delete("/documents/<int:doc_id>")
@jwt_required()
def delete_document(doc_id):
    d = Document.query.get_or_404(doc_id)
    fp = os.path.join(UPLOAD_FOLDER, d.stored_name)
    try:
        if os.path.exists(fp):
            os.remove(fp)
    except Exception:
        pass
    db.session.delete(d)
    db.session.commit()
    return {"status": "ok"}

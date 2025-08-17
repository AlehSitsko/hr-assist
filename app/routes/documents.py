# app/routes/documents.py
import os
from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.datastructures import FileStorage

from app.models import db, Employee, Document
from app.utils import allowed_file, secure_store_name

documents_bp = Blueprint("documents", __name__)

@documents_bp.post("/employees/<int:emp_id>/documents")
@jwt_required()
def upload_document(emp_id: int):
    # 1) сотрудник существует?
    employee = db.session.get(Employee, emp_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    # 2) файл в запросе?
    f: FileStorage | None = request.files.get("file")
    if not f or not f.filename:
        return jsonify({"error": "No file provided"}), 400

    # 3) расширение допустимо?
    if not allowed_file(f.filename):
        return jsonify({"error": "File type not allowed"}), 400

    # (опционально) базовый guard по mimetype для очевидных кейсов
    # if f.mimetype not in {"application/pdf", "image/jpeg", "image/png"}:
    #     return jsonify({"error": "MIME type not allowed"}), 400

    try:
        store_name = secure_store_name(f.filename)  # UUID.ext
    except ValueError:
        return jsonify({"error": "Invalid filename"}), 400

    upload_dir = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_dir, exist_ok=True)
    disk_path = os.path.join(upload_dir, store_name)

    try:
        # 4) сохраняем файл на диск
        f.save(disk_path)
        size_bytes = os.path.getsize(disk_path)

        # 5) запись в БД
        doc = Document(
            employee_id=emp_id,
            stored_name=store_name,
            original_name=f.filename,
            mimetype=f.mimetype,
            size_bytes=size_bytes,
        )
        db.session.add(doc)
        db.session.commit()

    except Exception as e:
        # если что-то пошло не так — чистим за собой
        db.session.rollback()
        with contextlib.suppress(Exception):
            if os.path.exists(disk_path):
                os.remove(disk_path)
        return jsonify({"error": str(e)}), 400

    return (
        jsonify(
            {
                "id": doc.id,
                "employee_id": emp_id,
                "original_name": doc.original_name,
                "stored_name": doc.stored_name,
                "mimetype": doc.mimetype,
                "size_bytes": doc.size_bytes,
                "uploaded_at": doc.uploaded_at.isoformat() if doc.uploaded_at else None,
            }
        ),
        201,
    )

@documents_bp.delete("/documents/<int:doc_id>")
@jwt_required()
def delete_document(doc_id: int):
    doc = db.session.get(Document, doc_id)
    if not doc:
        return jsonify({"error": "Document not found"}), 404

    upload_dir = current_app.config["UPLOAD_FOLDER"]
    disk_path = os.path.join(upload_dir, doc.stored_name)

    try:
        if os.path.exists(disk_path):
            os.remove(disk_path)
        db.session.delete(doc)
        db.session.commit()
        return jsonify({"message": "Document deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

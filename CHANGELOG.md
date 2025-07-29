# 📜 Changelog — HR Assist

All notable changes to this project will be documented in this file.

Format: [Added] / [Changed] / [Fixed] / [Removed] / [Security]

---

## [0.1.0] — 2025-07-29
### Initial Commit

- [Added] Flask project scaffold with:
  - `app/` folder and `__init__.py`
  - Basic `Employee` model with full certification tracking (CPR, EVOC, DL)
  - Config file (`config.py`)
  - Uploads folder structure
  - JWT-ready structure
  - Route folders: `routes/` and `auth/`
- [Added] Support for employee fields:
  - Personal data (name, phone, address, DOB, email)
  - Certification + expiration dates
  - Document path placeholder
  - `created_by`, `updated_by`, audit timestamps
- [Planned] Minimalist React frontend
- [Planned] Standalone version with Electron or PyWebView

---

## [Unreleased]
- Add full CRUD API for `Employee`
- Implement user authentication with JWT
- Add document upload and preview system
- Add certificate expiration checker
- Connect React frontend to backend API

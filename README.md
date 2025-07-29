# 🧾 HR Assist — Employee Certification & Document Tracker

## 📌 Overview

**HR Assist** is a lightweight internal web application built with **Flask** (backend) and **React** (frontend planned) for managing employee personal data, certifications, and uploaded documents.

This project is designed for **administrative use only** and is intended to run in a secure environment. Future versions will include a **standalone desktop version** (Electron or PyWebView).

---

## ⚙️ Features (MVP)

- ✅ Add/edit/delete employee records
- ✅ Track certification expirations (CPR, EVOC, Driver’s License)
- ✅ Store personal and employment data
- ✅ Upload and access scanned documents
- ✅ Admin-only authorization (JWT)
- ✅ API-ready architecture
- 🚧 Minimal React frontend (in progress)

---

## 📁 Project Structure

HR-assist/
├── app/ # Main application (models, routes, logic)
│ ├── models.py
│ ├── routes/
│ ├── utils.py
├── auth/ # Authentication (login, JWT)
├── uploads/ # Uploaded employee documents (PDF, JPG, etc.)
├── config.py # App configuration
├── run.py # Main entry point
├── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## 🛠 Installation

```bash
git clone https://github.com/YOUR_USERNAME/hr-assist.git
cd hr-assist

# Setup virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
🔐 Default Access
This app is intended for internal admin use only. User login and access roles will be configured manually for now.

📦 Tech Stack
Backend: Flask, SQLAlchemy, JWT

Frontend: React (planned)

Database: SQLite (MVP) → PostgreSQL (later)

Desktop: Electron / PyWebView (planned)

🚀 Roadmap
 MVP: Flask backend, REST API, employee model

 React admin frontend

 Document viewer / file manager

 Certification expiration reminders

 Admin dashboard & filters

 Standalone app (Electron or PyWebView)
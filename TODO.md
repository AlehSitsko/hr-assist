# ✅ TODO — HR Assist (Flask / React)

---

## 🔧 Core Backend

- [x] Set up Flask project structure
- [x] Create Employee model with all required fields
- [x] Configure database (SQLite for MVP)
- [x] Implement Employee CRUD API (GET, POST, PUT, DELETE)
- [x] Implement JWT protection for all API endpoints
- [x] Email uniqueness validation
- [x] Implement Auth login route and token issuance
- [ ] File upload logic (documents, certifications)
- [ ] Document retrieval endpoint
- [ ] Expiration check utilities (CPR, EVOC, DL)

---

## 🖥 Frontend (React Modular System)

- [ ] Initialize React frontend using Vite
- [ ] Implement login page with JWT auth
- [ ] Implement dashboard page (component selector)
- [ ] Set up routing for modules: HR, Scheduling, Call Taking, Patients
- [ ] Build HR module page (employee list/form)
- [ ] Add placeholder or embedded call-taking form
- [ ] Prepare structure for scheduling/hours module (WIP)
- [ ] Prepare structure for patient/trip database module (WIP)
- [ ] Ensure JWT token is passed to API requests

---

## 📦 Standalone Version

- [ ] Choose platform: Electron or PyWebView
- [ ] Package backend + frontend together
- [ ] Implement secure local storage
- [ ] Test offline functionality

---

## 🛡 Security / Access Control

- [x] Protect all API routes with JWT
- [x] Simple config-based login (no DB users)
- [ ] Restrict uploads by file type / size (planned)
- [ ] Sanitize filename inputs

---

## 🗂 Future Features

- [ ] Employee certification status dashboard
- [ ] Notifications: expiring/expired documents
- [ ] Document version history
- [ ] Multiple admin users
- [ ] Export to CSV / PDF
- [ ] Filter by active/inactive/expired

---

## 📝 Documentation

- [x] Create README.md
- [x] Create CHANGELOG.md
- [x] Create TODO.md
- [x] Dev log integrated into changelog
- [ ] Auto-generate API docs (Flasgger or ReDoc)

---

# ✅ TODO — HR Assist (Flask / React)

---

## 🔧 Core Backend

- [x] Set up Flask project structure
- [x] Create Employee model with all required fields
- [x] Configure database (SQLite for MVP)
- [x] Implement Employee CRUD API (GET, POST, PUT, DELETE)
- [x] Implement JWT protection for all API endpoints
- [x] Email uniqueness validation
- [ ] Implement Auth login route and token issuance
- [ ] File upload logic (documents, certifications)
- [ ] Document retrieval endpoint
- [ ] Expiration check utilities (CPR, EVOC, DL)

---

## 🖥 Frontend (Minimal React Admin Panel)

- [ ] Set up React project (Vite or CRA)
- [ ] Create login form (JWT auth)
- [ ] Create employee list + search
- [ ] Add employee form (create/edit)
- [ ] Document upload + view UI
- [ ] Expiration highlighting (color markers)
- [ ] Responsive minimal layout (optional)

---

## 📦 Standalone Version

- [ ] Choose platform: Electron or PyWebView
- [ ] Package backend + frontend together
- [ ] Implement secure local storage
- [ ] Test offline functionality

---

## 🛡 Security / Access Control

- [x] Protect all API routes with JWT
- [x] Restrict uploads by file type / size (planned)
- [ ] Auto-logout for inactive sessions (optional)
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

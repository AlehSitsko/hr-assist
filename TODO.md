# ✅ TODO — HR Assist (Flask / React)

---

## 🔧 Core Backend

- [x] Set up Flask project structure
- [x] Create `Employee` model with all required fields
- [x] Configure database (SQLite for MVP)
- [x] Implement full CRUD API for `Employee` (GET, POST, PUT, DELETE)
- [x] Implement JWT protection for all API endpoints
- [x] Email uniqueness validation (on POST)
- [x] Implement login route `/api/auth/login` with token issuance
- [ ] Add file upload logic (documents, certifications)
- [ ] Create endpoint for retrieving uploaded documents
- [ ] Add expiration check utilities (CPR, EVOC, DL)
- [ ] Add updated_by / created_by audit logic

---

## 🖥 Frontend (React Modular System)

- [x] Initialize React frontend with Vite
- [x] Implement login page with POST to `/api/auth/login`
- [x] Save JWT token to `localStorage` on success
- [x] Create `PrivateRoute.jsx` to protect `/dashboard`
- [x] Redirect to `/dashboard` after login
- [ ] Add logout button and clear token logic
- [ ] Build simple dashboard component (module selector)
- [ ] Set up router with fallback to `/login`
- [ ] Create reusable Navbar with username + logout
- [ ] Create `Employees.jsx` — employee list view
- [ ] Create employee add/edit form
- [ ] Connect frontend to GET / POST / PUT API
- [ ] Handle and display validation errors from backend
- [ ] Implement file upload field and view in employee form

---

## 🛡 Security / Access Control

- [x] All API endpoints require valid JWT
- [x] Config-based login credentials (no user DB)
- [ ] Sanitize filenames for uploads
- [ ] Restrict upload file types and max size
- [ ] Add token expiration auto-logout
- [ ] Handle unauthorized/expired token errors on frontend

---

## 🧪 Testing / QA / Polishing

- [ ] Add unit test for login flow
- [ ] Add integration test for `/api/employees`
- [ ] Test file uploads manually
- [ ] Manual UI testing (auth, form, errors)
- [ ] Finalize basic styling with Bootstrap
- [ ] Add spinner/loading indicator on login and form submit

---

## 📦 Standalone Version (Planned Phase)

- [ ] Choose runtime: Electron or PyWebView
- [ ] Bundle backend + frontend into one desktop package
- [ ] Setup secure local config and data storage
- [ ] Ensure offline usage possible

---

## 🗂 Future Features (Low Priority)

- [ ] Certification status dashboard (visual)
- [ ] Notifications for expiring/expired docs
- [ ] Document version tracking
- [ ] Multiple admin accounts
- [ ] Employee activity log
- [ ] Export employees to CSV or PDF
- [ ] Filter by certification status: active / expired / missing

---

## 📝 Documentation

- [x] Write README.md
- [x] Maintain CHANGELOG.md
- [x] Maintain structured TODO.md
- [x] Integrate developer notes in changelog
- [ ] Auto-generate API docs with Flasgger or ReDoc

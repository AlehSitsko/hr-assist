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

## [0.2.0] — 2025-07-31
### Backend API Complete (MVP)

- [Added] Full CRUD API for `Employee` (GET all, GET by ID, POST, PUT, DELETE)
- [Added] Universal serialization method (`serialize_employee`) to replace `__dict__`
- [Changed] All endpoints now require JWT authentication with `@jwt_required()`
- [Added] Email uniqueness check on creation (`POST /employees`)
- [Added] `GET /employees/<id>` endpoint for fetching single employee
- [Changed] `updated_at` field now auto-updated on PUT
- [Planned] Auth endpoint `POST /auth/login` with JWT issuance

🗓 **Dev Log**:
> "Возвращаюсь к проекту после короткой паузы на основной работе. Решил привести employees.py к финальной форме, сделать его максимально читаемым и безопасным. Добавил защиту маршрутов и универсальную сериализацию. Сюда же начал фиксировать ключевые действия — чтобы было проще восстановить контекст через день или неделю."

---

## [0.2.1] — 2025-07-31
### Minimal Auth System

- [Added] Simple hardcoded login: username = "Welcome", password = "Utop1631"
- [Added] JWT token issuance via `POST /api/auth/login`
- [Security] All endpoints continue to require valid JWT access token

🗓 **Dev Log**:
> "Решено не использовать email и базу пользователей — авторизация реализована просто и надёжно. Весь проект работает в оффлайн-среде на 1–2 ПК, поэтому базовая защита логина/пароля вполне оправдана. На всё ушло меньше 10 минут."

✅ Changes successfully pushed to `dev` and merged into `main`.

---

## [0.3.0] — 2025-07-31
### Frontend Structure Approved

- [Planned] Modular architecture with Component Selector Dashboard
- [Planned] Separate pages for:
  - HR Management
  - Scheduling & Hours
  - Call Taking (with embedded printable form)
  - Patients & Trips (future DB-driven logic)
- [Planned] Each module may use its own DB/backend blueprint
- [Planned] React/Vite frontend layout:
  - `Login` page with JWT auth
  - `Dashboard` with component grid (select module)
  - Component-specific routes and views
### Frontend Structure 
[Login Page] 
   ↓
[Component Selector (Dashboard)]
   ↓
[HR]      [Scheduling]      [Call Taking]      [Patients / Trips]

🗓 **Dev Log**:
> "Я решил не делать монолитную форму, а разбить интерфейс на модули. Это даёт масштабируемость: можно подключать независимые компоненты, каждый с отдельной логикой, API, и даже базой. Начнём с HR и подключим остальное по мере развития."

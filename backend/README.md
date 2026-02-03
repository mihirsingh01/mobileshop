# Backend - Mobile Shop

This README describes the current status of the backend, what has been implemented so far, how to run and test it locally, important files and directories, and suggested next steps.

## Project overview

- Framework: Django
- Database: SQLite (file `db.sqlite3` in the backend root)
- Purpose: Backend for a mobile shop application with multiple Django apps handling authentication, customers, sales, repairs, staff roles, and accessories.

## What has been done so far

- Basic Django project scaffold created (`mobile_shop_backend` Django project).
- Multiple Django apps added and scaffolded with models, views, urls, and admin registration:
  - `logins` (authentication and login forms/views)
  - `customer`
  - `sales`
  - `repairing_staff`
  - `promoter_staff`
  - `accessories_staff`
  - `old_mobile_staff`
  - `promoter_staff`
  - `super_admin`
  - `cashier`
- Migrations are present for several apps in their `migrations/` directories.
- Templates and form code exist (e.g., `logins/forms.py`, `super_admin/forms.py`, and `logins/templates` may exist for login pages).
- `manage.py` available for running the development server and Django management commands.

## Important files and directories

- `manage.py` - Django management utility.
- `db.sqlite3` - Development SQLite database file (already present).
- `mobile_shop_backend/` - Django project settings and WSGI/ASGI entrypoints.
  - `settings.py` - main Django settings (inspect for database, static files, installed apps).
  - `urls.py` - project URL configuration.
- App directories (each contains `models.py`, `views.py`, `urls.py`, `admin.py`, `tests.py`, and `migrations/`).
- `requirements.txt` - Python dependencies for the project.

## How to run the backend locally (development)

1. Create a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run database migrations (if needed):

```powershell
python manage.py migrate
```

4. Create a superuser (optional, to access admin):

```powershell
python manage.py createsuperuser
```

5. Start the development server:

```powershell
python manage.py runserver
```

6. Open http://127.0.0.1:8000/ in your browser. The admin site is typically at `/admin/`.

Note: The repository already contains `db.sqlite3` and some migrations; if you want a clean database, remove `db.sqlite3` and re-run steps 3-4.

## Notes about the codebase

- Apps are organized by functional area (staff roles, customer, sales, accessories).
- Check each app's `models.py` to see data schema and relationships.
- Forms and templates support login and admin flows; inspect `logins/forms.py` and `logins/views.py` for authentication logic.
- There may be some unused or legacy code (e.g., `old_mobile_staff`) left for reference.

## Next steps / Suggestions

- Add a `README.md` per app explaining each app's responsibility and API endpoints.
- Add automated tests for critical flows in `tests.py` files.
- Move sensitive settings out of `settings.py` and use environment variables for production.
- Set up Docker and a proper development DB (Postgres) for parity with production.
- Implement API documentation (Swagger / DRF schema) if converting to REST API.

## Who to contact

- Repository owner / primary developer: mihirsingh01

---

If you'd like, I can:
- Expand this README with details from specific files (I can scan `settings.py`, `logins/forms.py`, and `mobile_shop_backend/urls.py`).
- Create per-app READMEs.
- Add a `Makefile` or PowerShell scripts to simplify local dev commands.

Tell me what else you'd like included and I will update the README.

# Deployment Guide for Mobile Shop Project on cPanel Using GitHub

This guide explains how to deploy the Django backend and React frontend to the cPanel subdomain `mobileshop.itechgurusolution.xyz` using a GitHub repository.

## Prerequisites
- Access to cPanel with the provided credentials.
- A GitHub repository containing the project code.
- The subdomain `mobileshop.itechgurusolution.xyz` is set up in cPanel, pointing to `/home/hrms.itechgurusolution.xyz/mobileshop.itechgurusolution.xyz/`.
- Python and Passenger are enabled in cPanel.

## Steps

### 1. Push Code to GitHub
- Ensure all project files, including `backend/`, `frontend/`, `.cpanel.yml`, `requirements.txt`, `passenger_wsgi.py`, and updated `settings.py`, are committed and pushed to your GitHub repository.

### 2. Set Up Git Version Control in cPanel
- Log in to cPanel.
- Go to **Git™ Version Control** under **Files**.
- Click **Create** to add a new repository.
- **Clone URL**: Enter your GitHub repository URL (e.g., `https://github.com/username/mobile_shop.git`).
- **Repository Path**: Set to `/home/itechgurusolutio/repositories/mobile_shop` or similar.
- **Repository Name**: `mobile_shop`.
- Click **Create**.
- After cloning, go to **Manage** for the repository.
- Under **Deployment**, set **Deployment Path** to `/home/hrms.itechgurusolution.xyz/mobileshop.itechgurusolution.xyz/`.
- Enable **Automatic Deployment** if desired, or deploy manually.
- The `.cpanel.yml` file will be used for deployment tasks, copying files to the deployment path.

### 3. Configure Python Application
- In cPanel, go to **Setup Python App**.
- Create a new application:
  - **App Directory**: `/home/hrms.itechgurusolution.xyz/mobileshop.itechgurusolution.xyz/backend`
  - **App URI**: `/` (root for the subdomain)
  - **Passenger log file**: Set as needed.
  - **Python version**: Select a compatible version (e.g., 3.8 or higher).
  - **Startup file**: `passenger_wsgi.py`
  - **Application URL**: `mobileshop.itechgurusolution.xyz`
- Install requirements: In the app setup, it will use `requirements.txt` automatically.

### 4. Database and Static Files
- SSH into the server or use cPanel Terminal.
- Navigate to the backend directory: `cd /home/hrms.itechgurusolution.xyz/mobileshop.itechgurusolution.xyz/backend`
- Run migrations: `python manage.py migrate`
- Collect static files: `python manage.py collectstatic --noinput`

### 5. Frontend Deployment
- Build the React frontend: In the `frontend` directory, run `npm run build`.
- Copy the `build` folder contents to the static files directory or serve separately.
- If serving from Django, place in `backend/staticfiles/` or configure accordingly.
- For separate hosting, upload to a different subdomain or use cPanel's File Manager to serve static files.

### 6. Environment Variables
- Set any necessary environment variables in cPanel's **Environment** section for the Python app, e.g., `DJANGO_SETTINGS_MODULE=mobile_shop_backend.settings`.

### 7. Test the Deployment
- Visit `https://mobileshop.itechgurusolution.xyz` to test the backend.
- Ensure all endpoints work and static files are served.

## Notes
- The backend uses SQLite, so no external database setup is needed.
- If issues arise, check Passenger logs in cPanel.
- For production, update `SECRET_KEY` in `settings.py`.
- Ensure `ALLOWED_HOSTS` includes the subdomain.

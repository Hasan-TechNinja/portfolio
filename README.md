# Django Fullstack Portfolio

A modern, responsive, and dynamic portfolio built with Django, featuring a glassmorphism design, typing animations, and an interactive project showcase.

---

## Free Deployment Guide on PythonAnywhere

Follow these step-by-step instructions to deploy this Django project online for free using [PythonAnywhere](https://www.pythonanywhere.com/).

### Step 1: Create a PythonAnywhere Account
1. Go to [PythonAnywhere](https://www.pythonanywhere.com/) and click **Pricing & signup**.
2. Create a **Beginner account** (it's 100% free).
3. Log into your dashboard.

### Step 2: Open a Bash Console
1. On your PythonAnywhere Dashboard, go to the **Consoles** tab.
2. Click on **Bash** under "Start a new console".

### Step 3: Clone the Repository
In the Bash console, clone the GitHub repository and navigate into it:
```bash
git clone https://github.com/Hasan-TechNinja/portfolio.git
cd portfolio
```
*(Note: Replace the URL with the actual repository URL if you have forked it).*

### Step 4: Environment Variables Setup
Create a `.env` file from the provided example and configure your variables:
```bash
cp .env.example .env
nano .env
```

Here is the structure of the `.env.example` file that you need to fill out:
```env
# Database Configuration (PostgreSQL)
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

# Email & SMTP Configuration
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_USE_SSL=

# Replace with your email address and App Password
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=

DEBUG=False
```
*(Save and exit the editor when you are done).*

### Step 5: Create & Activate a Virtual Environment
Create a virtual environment using Python 3.12 and activate it:
```bash
python3.12 -m venv env
source env/bin/activate
```

### Step 6: Run the Build Script
We have included a build script that will automatically install dependencies, collect static files, and apply database migrations. Run it with:
```bash
chmod +x build.sh
./build.sh
```

### Step 7: Create an Admin Superuser
Create an admin account to manage your portfolio content:
```bash
python manage.py createsuperuser
```
*(Follow the prompts to input your username, email, and password).*

### Step 8: Setup the Web App in PythonAnywhere
1. Go to the **Web** tab in PythonAnywhere.
2. Click **Add a new web app**.
3. Click **Next**, then select **Manual configuration (including virtualenvs)** (⚠️ Do *not* select Django).
4. Select **Python 3.12** (to match the virtual environment we created).
5. Click **Next** to finish creating the app.

### Step 9: Configure Virtualenv & Source Code Paths
Still on the **Web** tab, scroll down to configure:
1. **Source code:** Set this to `/home/yourusername/portfolio`
2. **Virtualenv:** Set this to `/home/yourusername/portfolio/env`

### Step 10: Configure the WSGI File
1. On the **Web** tab, scroll to the **Code** section.
2. Click the link next to **WSGI configuration file** (it looks like `/var/www/yourusername_pythonanywhere_com_wsgi.py`).
3. Delete everything in that file and paste the following:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/portfolio'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

# Serve the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
*(Make sure to change `yourusername` to your actual PythonAnywhere username, and `portfolio.settings` to your project's main settings folder name if it's different).*

4. Click **Save** in the top right.

### Step 11: Setup Static & Media Files
Go back to the **Web** tab and scroll down to the **Static files** section. Add two entries to ensure CSS, JS, and Images load properly:

1. **Static Files:**
   - **URL:** `/static/`
   - **Directory:** `/home/yourusername/portfolio/staticfiles/` (or `/home/yourusername/portfolio/static/` depending on your setup).

2. **Media Files:**
   - **URL:** `/media/`
   - **Directory:** `/home/yourusername/portfolio/media/`

### Step 12: Reload and Go Live!
1. Scroll to the very top of the **Web** tab.
2. Click the big green **Reload yourusername.pythonanywhere.com** button.
3. Click the link above the button to visit your live portfolio!

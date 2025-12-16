# 📘 Django Blog Authentication System Documentation

## 1. System Overview
This module provides a secure and user-friendly authentication system for the Django Blog application. It allows users to:
* **Register** a new account with a username and password.
* **Login** to access restricted features.
* **Logout** securely.
* **Manage Profile** (Update Username and Email).

The system leverages Django's built-in `User` model for robust security (including password hashing) while implementing custom views and forms for a tailored user experience.

---

## 2. Setup Instructions

### Prerequisites
Ensure you have the following installed:
* Python 3.x
* Django 5.0+

### Installation & Configuration

#### Database Migrations
The authentication system relies on the default Django `auth_user` table. Run migrations to create these tables:

```bash
python manage.py migrate

# Redirect to the homepage after successful login
LOGIN_REDIRECT_URL = 'home' 

# Redirect to the login page after logout
LOGOUT_REDIRECT_URL = 'login'

#### URL Configuration (`blog/urls.py`)
Ensure the following paths are defined in your app-level `urls.py`:

```python
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Custom Views
    path('register/', views.register, name='register'),
    path('profile/', views.ProfileView, name='profile'),

    # Built-in Django Auth Views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]

4. User Guide
How to Register
Navigate to the Register link in the navigation bar.

Enter a unique username.

Enter a strong password (must meet Django's complexity requirements).

Confirm the password.

Click Sign Up. You will be redirected to the login page.

How to Login
Click Login in the navigation bar.

Enter your Username and Password.

Upon success, you will be redirected to the Home page.

The navigation bar will change to show "Profile" and "Logout".

How to Edit Profile
Login to the application.

Click the Profile link in the navigation bar.

You will see your current Username and Email pre-filled.

Change the desired fields.

Click Update Info.

A success message "Your profile has been updated!" will appear.

5. Troubleshooting Common Issues
Error: TemplateDoesNotExist at /login/

Fix: Ensure your login template is specifically located at blog/templates/registration/login.html. Django looks for the registration folder by default.

Error: CSRF verification failed

Fix: Ensure every <form method="POST"> in your templates includes the {% csrf_token %} tag.

Error: Profile form is empty (No fields)

Fix: Ensure blog/views.py is passing the context dictionary correctly: {'form': form} and that forms.py has fields = ['username', 'email'].
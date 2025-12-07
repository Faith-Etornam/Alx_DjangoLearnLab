### Authentication System Documentation

This document explains how the authentication system in my Django Blog Application works. It covers registration, login, logout, and profile management, how users interact with each feature and finally the testing steps for each part are also included.

## Overview of Authentication System

The application uses Django’s built-in authentication framework to manage:
    User registration
    User login
    User logout
    Profile viewing and editing
    Authentication protection for restricted pages

## Authentication Features
# Registration (Sign Up)
How It Works:
    Users create an account using a custom registration form (RegisterForm) that extends Django’s UserCreationForm.

Workflow:
    User opens blog/register/
    They fill in username, password, and email
    If the form is valid:
        A new user is created
    The user is automatically logged in (via login(request, user))
    They are redirected to their profile page

View Used:
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})


## Login
Logout uses Django’s built-in 'LoginView'.

How It Works:
    The login system uses Django’s built-in authentication views.

URL:
/blog/login/

Template displays {{ form }} and prompts for:
    username, email, and password

If authentication succeeds, Users are redirect to profile
If it fails error message is displayed.

Testing Authentication:
    Use a valid username, email and password: should log in successfully
    Use invalid credentials: form should show errors


## Logout
Logout uses Django’s built-in 'LogoutView'.

URL:
    /blog/logout/

After logout, usesr are redirected to a logout confirmation or home page.


## Profile (View & Edit)
This page requires users to be logged in.
How It Works:
    Users must authenticate first. This is enforced with the Django decorator - '@login_required'.
    Users see their profile details: username, email
    Users can update the profile through a POST request
    Successful updates trigger a message using Django’s messages framework

View Used:
@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile')

    return render(request, 'blog/profile.html', {'user': user})

## URL Configuration
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # Django built-in auth views
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]

## Templates Overview
Templates implemented:
File:	                    Purpose:
    base.html	                Main layout (CSS, messages, structure)
    register.html	            User registration page
    login.html	                User login page
    logout.html	                Logout confirmation
    profile.html	            Profile view & edit


## How Users Interact With Authentication

# Registration Flow
    Visit /blog/register/
    Fill out form → click Register
    User auto-logged in
    Redirect to /blog/profile/

# Login Flow
    Visit /blog/login/
    Enter credentials
    Redirect to Profile

# Logout Flow
    Visit /blog/logout/
    User session ends
    Redirect to logout page

# Profile Flow
    Must be logged in
    View /blog/profile/
    Update details
    Changes saved in database

# Testing Authentication Features
    Below are step-by-step instructions for manual testing.


## Test Registration
    Go to /blog/register/
    Enter username, email, and password twice
    Expected results:
        New user is created
        User is automatically logged in
        Redirect to /blog/profile/
        Confirm user appears in database:

python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()

## Test Login
    Go to /blog/login/
    Enter correct credentials
    Should redirect to profile
    Enter wrong credentials
    Should show error message

## Test Logout
    Login first
    Go to /blog/logout/
    Expected result:
        Session ends
    User cannot access /blog/profile/ unless logged in

## Test Profile Update
    Login and visit /blog/profile/
    Update:
    Usernname
    Email
    Expected results:
        Success message appears
        Updated values saved in database
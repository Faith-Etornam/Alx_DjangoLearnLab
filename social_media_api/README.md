# Project Setup

## Clone the repository:

git clone https://github.com/DannyTechStudio/Alx_DjangoLearnLab.git
cd project_dir


## Create and activate a virtual environment:

python -m venv env
# On Windows
.\env\Scripts\activate
# On macOS/Linux
source env/bin/activate


## Install dependencies:

Environment & Dependencies

Python 3.10+
Django 6.0
Django REST Framework
djangorestframework.authtoken

Make sure to add the following apps to INSTALLED_APPS in settings.py:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'users',
]

## Database Migration

Run the following commands to apply migrations:

python manage.py makemigrations
python manage.py migrate

Running the Server

Start the development server:

python manage.py runserver

Your API will be available at http://127.0.0.1:8000/.


## User Authentication

The API uses DRF Token Authentication. Each registered user is issued a unique token to access protected endpoints.

Register a User:

Endpoint: POST /api/auth/register/
Request Body:
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "strongpassword",
  "bio": "Hello, I'm John!",
  "profile_picture": "<image-file>"
}

Response:
{
  "user": {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "bio": "Hello, I'm John!"
  },
  "token": "<user-token>"
}


Login
Endpoint: POST /api/auth/login/
Request Body:
{
  "username": "johndoe",
  "password": "strongpassword"
}

Response:
{
  "user": {
    "username": "johndoe",
    "email": "johndoe@example.com"
  },
  "token": "<user-token>"
}

Retrieve Profile

Endpoint: GET /api/auth/me/
Headers: Authorization: Token <user-token>

Response:
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "bio": "Hello, I'm John!",
  "profile_picture": "http://127.0.0.1:8000/media/profiles/johndoe.png"
}

Logout

Endpoint: POST /api/auth/logout/
Headers: Authorization: Token <user-token>

Response:
{
  "detail": "Logout successful"
}

Note: Logout deletes the token, so the user must log in again to receive a new token.


## COMMENTS API

### 1. List Comments
GET /api/comments/

### 2. Retrieve Comment
GET /api/comments/{id}/

### 3. Create Comment
POST /api/comments/
Content-Type: application/json

{
"post": 1,
"content": "Nice post!"
}

### 4. Update Comment
PUT /api/comments/{id}/

### 5. Delete Comment
DELETE /api/comments/{id}/

### API Test Requests (.http file)

### ---------------------------
### POSTS ENDPOINT TESTS
### ---------------------------

# Get first page of posts
GET http://127.0.0.1:8000/api/posts/
Accept: application/json

###
# Get second page of posts
GET http://127.0.0.1:8000/api/posts/?page=2
Accept: application/json

###
# Get posts with custom page size
GET http://127.0.0.1:8000/api/posts/?page=1&page_size=20
Accept: application/json

###
# Search posts (title or content)
GET http://127.0.0.1:8000/api/posts/?search=django
Accept: application/json

###
# Combine search + pagination
GET http://127.0.0.1:8000/api/posts/?search=api&page=2
Accept: application/json

### ---------------------------
### COMMENTS ENDPOINT TESTS
### ---------------------------

# Get comments (first page)
GET http://127.0.0.1:8000/api/comments/
Accept: application/json

###
# Get page 3 of comments
GET http://127.0.0.1:8000/api/comments/?page=3
Accept: application/json

###
# Combine search (if added later) + pagination
GET http://127.0.0.1:8000/api/comments/?search=nice&page=1
Accept: application/json

## LIKE A POST

POST /api/posts/{id}/like/
Request Headers:
Authorization: Token <your_token>

Response (201 Created):
{
  "detail": "Post liked."
}

If already liked (400):
{
  "detail": "You've already liked this post."
}

## UNLIKE A POST

Endpoint to remove a like from a post.

POST /api/posts/{id}/unlike/
Success:
{
  "detail": "Post unliked."
}

If post wasn’t liked:
{
  "detail": "You have not liked this post."
}

## Notifications Documentation
## GET Notifications
GET /api/notifications/

Returns all notifications for the authenticated user.

Example Response:
[
  {
    "id": 1,
    "recipient": "johndoe",
    "actor": "mary",
    "verb": "liked your post",
    "timestamp": "2025-01-10T14:22:54Z",
    "target": {
      "type": "post",
      "id": 14
    },
    "read": false
  }
]

## Mark Notification as Read
POST /api/notifications/{id}/read/
Response:
{ "detail": "Notification marked as read." }

## Mark All Notifications as Read
POST /api/notifications/mark-all-read/
Response:
{ "detail": "All notifications marked as read." }
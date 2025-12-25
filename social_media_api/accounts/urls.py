from django.urls import path
from .views import Register, Profile, Login

urlpatterns = [
    path('register/', Register.as_view(), name='registration'),
    path('login/', Login),
    path('profile/', Profile)
]



from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books 
from .views import LibraryDetailView
from . import views

urlpatterns = [
    path('books/', list_books),
    path('libraries/<int:pk>', LibraryDetailView.as_view()),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html')),
    path('register/', views.register, name='register'),b
]

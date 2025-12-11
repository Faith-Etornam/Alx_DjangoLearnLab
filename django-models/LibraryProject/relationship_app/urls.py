from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books 
from .views import LibraryDetailView, RegisterView
from . import views

urlpatterns = [
    path('books/', list_books),
    path('libraries/<pk:int>', LibraryDetailView.as_view()),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html', name='logout')),
    path('register/', views.register, name='register')
]

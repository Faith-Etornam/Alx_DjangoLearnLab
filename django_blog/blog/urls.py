from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html')),
    path('profile/', views.profileView, name='profile'),
    path('posts/', views.ListView.as_view(), name='posts'),
    path('posts/<int:pk>', views.BlogDetailView.as_view(), name='post_detail')
]

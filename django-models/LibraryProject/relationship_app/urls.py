from django.urls import path
from .views import list_books, LibraryDetailView, register_view, login_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/',views.register,  name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('books/', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('edit_books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]

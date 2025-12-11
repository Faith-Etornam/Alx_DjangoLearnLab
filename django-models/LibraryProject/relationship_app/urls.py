from django.urls import path
from .views import list_books 
from .views import LibraryDetailView, LogoutView, LoginView

urlpatterns = [
    path('books/', list_books),
    path('libraries/<pk>', LibraryDetailView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]

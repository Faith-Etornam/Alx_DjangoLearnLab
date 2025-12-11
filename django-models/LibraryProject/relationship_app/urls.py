from django.urls import path
from .views import list_books 
from .views import LibraryDetailView

urlpatterns = [
    path('books/', list_books),
    path('libraries/<pk>', LibraryDetailView.as_view())
]

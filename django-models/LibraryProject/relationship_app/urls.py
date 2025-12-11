from django.urls import path
from .views import book_lists 
from .views import LibraryDetailView

urlpatterns = [
    path('books/', book_lists),
    path('libraries/<pk>', LibraryDetailView.as_view())
]

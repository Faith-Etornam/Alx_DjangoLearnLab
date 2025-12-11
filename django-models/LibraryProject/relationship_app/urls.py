from django.urls import path
from .views import book_list 
from .views import LibraryDetailView

urlpatterns = [
    path('books/', book_list),
    path('libraries/<pk>', LibraryDetailView.as_view())
]

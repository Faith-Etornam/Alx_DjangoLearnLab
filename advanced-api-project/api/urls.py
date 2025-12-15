from django.urls import path
from .views import ListView, CreateView

urlpatterns = [
    path('books/', ListView.as_view(), name='list-book'),
    path('books/create', CreateView.as_view(), name='create-book')
]

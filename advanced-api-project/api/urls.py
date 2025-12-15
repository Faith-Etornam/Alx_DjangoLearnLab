from django.urls import path
from .views import ListView, CreateView, UpdateView, DeleteView, DetailView

urlpatterns = [
    path('books/', ListView.as_view(), name='list-book'),
    path('books/<int:pk>', DetailView.as_view(), name='detail-book'),
    path('books/create', CreateView.as_view(), name='create-book'),
    path('books/<int:pk>/update/', UpdateView.as_view(), name='update-book'),
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='delete-book')
]

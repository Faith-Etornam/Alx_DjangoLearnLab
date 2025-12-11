from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    path('books/', book_list),
    path('libraries/<pk>', LibraryDetailView.as_view())
]

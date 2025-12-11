from django.urls import path
from .views import book_list, LibraryDetail

urlpatterns = [
    path('books/', book_list),
    path('libraries/<pk>', LibraryDetail.as_view())
]

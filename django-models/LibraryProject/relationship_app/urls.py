from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('libraries/<pk>', views.LibraryDetail.as_view())
]

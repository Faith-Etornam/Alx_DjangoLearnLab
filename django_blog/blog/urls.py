from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html')),
    path('profile/', views.profileView, name='profile'),
    path('posts/', views.ListView.as_view(), name='posts'),
    path('post/new/', views.CreateView.as_view(), name='posts_create'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view() ,name='delete-post'),
    path('post/<int:pk>/update/', views.BlogUpdateView.as_view() ,name='delete-post'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    
    path('search/', views.PostSearchView.as_view(), name='search_posts'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),

]

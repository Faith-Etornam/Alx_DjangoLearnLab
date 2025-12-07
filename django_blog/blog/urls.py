from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import PostSearchView, PostByTagListView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),           #--------- Login (built-in)
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),       #--------- Logout (built-in
    path('register/', register, name='register'),       #--------- Registration (custom)
    path('profile/', profile, name='profile'),          #--------- Profile page
    
    #----- Posts
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    #----  Comments
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    
    path('search/', PostSearchView.as_view(), name='search_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]

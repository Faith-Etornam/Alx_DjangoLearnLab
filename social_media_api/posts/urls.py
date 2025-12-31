from django.urls import path
from .views import UserFeedView, LikePostView, 

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path("post/<int:pk>/like/", LikePostView.as_view(), name="like-post"),
]

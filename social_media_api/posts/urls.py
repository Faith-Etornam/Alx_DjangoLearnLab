from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewset, CommentViewset, UserFeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewset)
router.register(r'comments', CommentViewset)


urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path("post/<int:pk>/like/", LikePostView.as_view(), name="like-post"),
    path("post/<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike-post"),
]

urlpatterns += router.urls
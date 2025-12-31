from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from posts.models import Comment, Post, Like
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from .paginations import PostPagination
from notifications.models import Notification

# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    
    def create(self, serializer):
        serializer.save(author=self.request.user)
class Comments(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

class UserFeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        
        following_users = request.user.following.all()

        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    



class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)
        
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response({
                "detail": "You've already liked this post."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                content_type=ContentType.objects.get_for_model(Post),
                object_id=post.id
            )

        return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)



from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from posts.models import Comment, Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from .paginations import PostPagination

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


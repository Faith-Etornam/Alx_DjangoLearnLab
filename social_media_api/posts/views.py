from django.shortcuts import render
from posts.models import Comment, Post
from rest_framework import viewsets

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


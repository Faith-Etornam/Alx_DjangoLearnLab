from django.shortcuts import render
from posts.models import Comment, Post
from rest_framework import viewsets

# Create your views here.

class Posts(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    # serializer_class = 

class Comments(viewsets.ModelViewSet):
    queryset = Comment.objects.all()


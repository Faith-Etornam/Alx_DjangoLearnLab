from django.shortcuts import render
from posts.models import Comment, Post
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

# Create your views here.

class Posts(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    # serializer_class = 

class Comments(ModelViewSet):
    queryset = Comment.objects.all()


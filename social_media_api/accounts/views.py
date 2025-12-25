from django.shortcuts import render
from posts.models import Comment, Post
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

# Create your views here.

class Register(CreateAPIView):
    pass

class Login():
    pass

class Profile():
    pass
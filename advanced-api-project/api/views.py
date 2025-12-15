from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from rest_framework import filters
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

class ListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', 'publication_year', 'author']
    search_fields = ['title', 'author']

class DetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class CreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

class UpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()







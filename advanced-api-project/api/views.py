from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class ListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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







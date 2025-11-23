from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book 
from .permissions import IsOwnwerOrReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
      
        
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwnwerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)       # Automatically set the author to the logged-in user
        

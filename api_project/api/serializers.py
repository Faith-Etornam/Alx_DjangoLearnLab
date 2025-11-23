from rest_framework import serializers
from .models import Book

# ---------------------------
# BOOK SERIALIZER
# ---------------------------
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
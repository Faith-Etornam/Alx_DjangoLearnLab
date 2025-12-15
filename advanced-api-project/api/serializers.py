from django.utils.timezone import now
from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > now().year:
            raise serializers.ValidationError('Year cannot be greater than the current year')
        
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) 
    class Meta:
        model = Author
        fields = '__all__'

        

        
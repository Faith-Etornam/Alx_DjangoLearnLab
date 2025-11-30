from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

#---------- Class Serializers
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        
    def validate(self, data):
        publication_year = data.get('publication_year')
        if publication_year:
            current_year = datetime.now().year
            if data['publication_year'] > current_year:
                raise serializers.ValidationError("Pubication year must not be in the future!")
        return data
    

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name']
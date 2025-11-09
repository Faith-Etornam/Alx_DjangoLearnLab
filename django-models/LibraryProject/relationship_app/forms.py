from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_date', 'description']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'isbn': 'ISBN',
            'publication_date': 'Publication Date',
            'description': 'Description',
        }
    
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        # Basic ISBN validation (10 or 13 digits)
        if len(isbn) not in [10, 13]:
            raise forms.ValidationError('ISBN must be 10 or 13 characters long.')
        return isbn
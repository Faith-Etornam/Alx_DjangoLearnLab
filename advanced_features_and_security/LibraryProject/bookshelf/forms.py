from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]
        
    def clean_title(self):
        title = self.cleaned_data["title"]
        # Example simple sanitization / validation
        if "<script" in title.lower():
            raise forms.ValidationError("Invalid characters in title.")
        return title.strip()

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
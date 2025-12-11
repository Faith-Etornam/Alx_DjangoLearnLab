from django.http import HttpResponse
from .models import Book, Author
from django.shortcuts import render


# Create your views here.
def book_list(request):
    queryset = Book.objects.all()
    context = {'books': queryset}
    return render(request, 'relationship_app/list_books.html', context)
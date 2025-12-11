from django.http import HttpResponse
from .models import Book, Author
from django.shortcuts import render


# Create your views here.
def book_list(request):
    queryset = Book.objects.all()
    Author.objects.create(name="Stan Lee")
    Author.objects.create(name="Stan Pee")
    Book.objects.create(title='Spider-Man', author_id=1)
    Book.objects.create(title='Iron-Man', author_id=1)
    Book.objects.create(title='Captain America', author_id=1)
    context = {'books': queryset}
    return render(request, 'list_books.html', context)
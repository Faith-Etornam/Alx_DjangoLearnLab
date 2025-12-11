from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from .models import Library


# Create your views here.
def book_list(request):
    queryset = Book.objects.all()
    context = {'books': queryset}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    library = Library.objects.get(id=1)
    books = Book.objects.filter(id__in=[1, 2, 3])
    library.books.set(books)

class LibraryList(ListView):
    model = Library
    


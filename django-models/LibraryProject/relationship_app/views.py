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

class BookDetail(DetailView):
    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['id'])


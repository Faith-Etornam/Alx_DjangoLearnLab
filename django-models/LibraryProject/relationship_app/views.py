from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Book
from .models import Library


# Create your views here.
def list_books(request):
    queryset = Book.objects.all()
    context = {'books': queryset}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'relationship_app/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})




from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.detail import DetailView
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
    
def is_admin(user):
    return user.profile.role == 'Admin'

def is_member(user):
    return user.profile.role == 'Member'

def is_librarian(user):
        return user.profile.role == 'Librarian'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def admin_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def admin_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book',raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        author = Book.objects.update(title=title, author=author)
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html')









# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'



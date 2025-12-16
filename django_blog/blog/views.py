from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView as BlogListView
from .models import Post
from .forms import RegisterForm, UserUpdateForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

def account(request):
    return render(request, 'blog/profile.html')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('home')

class ListView(BlogListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

@login_required
def profileView(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('home')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'blog/profile.html', {'form': form})






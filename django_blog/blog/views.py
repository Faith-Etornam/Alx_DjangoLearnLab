from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm, UserUpdateForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

def account(request):
    return render(request, 'blog/profile.html')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'blog/registration.html'
    success_url = reverse_lazy('home')

@login_required
def profileView(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'blog/profile.html', {'form': form})


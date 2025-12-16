from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'blog/registration.html'
    success_url = reverse_lazy('home')

@login_required
def ProfileView(request):
    if request.method == 'POST':



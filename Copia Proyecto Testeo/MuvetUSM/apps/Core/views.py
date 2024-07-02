from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistroUsuario, IniciarUsuario


# Create your views here.

@login_required
def home(request):
    return render(request, 'Core/home.html')

def homeprof(request):
    return render(request, 'Core/homeprof.html')

class CustomLogoutView(LogoutView):
    # template_name = 'logout.html'  # optional
    next_page = reverse_lazy('home')

    def get(self, request):
        # Add any custom logic here, e.g., clearing session data
        return super().get(request)
    
class resetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Correo electrónico'

    def get_users(self, correo):
        email_field_name = Usuario._meta.get_field('correo').name
        users = Usuario._default_manager.filter(**{
            email_field_name + '__iexact': correo
        })
        return users
    
"""class CustomLoginView(LoginView):
    # template_name = 'logout.html'  # optional
    next_page = reverse_lazy('home')

    def get(self, request):
        # Add any custom logic here, e.g., clearing session data
        return super().get(request)
"""

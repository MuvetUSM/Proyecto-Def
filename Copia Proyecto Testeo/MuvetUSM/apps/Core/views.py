from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistroUsuario, IniciarUsuario

# Create your views here.

def registrar(request):
    data = {
        'form': RegistroUsuario()
    }

    if request.method == "POST":
        user_creation_form = RegistroUsuario(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('home')

    return render(request, 'Core/registrodeUsuario.html', data)
def home(request):
    return render(request, 'Core/home.html')

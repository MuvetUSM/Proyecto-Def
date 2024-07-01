from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Usuario, Curso
from .forms import RegistroUsuario, IniciarUsuario, EditCursoForm

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

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'Core/cursos.html', {'cursos': cursos})

def edicion(request, name):
    curso = get_object_or_404(Curso, name=name)
    
    if request.method == 'POST':
        form = EditCursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos') 
    else:
        form = EditCursoForm(instance=curso)
    
    return render(request, 'Core/edicion.html', {'form': form})


def eliminar(request, name):
    curso = get_object_or_404(Curso, name=name)
    curso.delete()
    return redirect('cursos') 
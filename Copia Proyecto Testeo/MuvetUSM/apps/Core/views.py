from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import *
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

#cursos    
def creacion_curso(request):
    return render(request, 'cursos/creacion_curso.html')
def generacion_curso(request):
    data_creacion = request.POST
    numeracion = data_creacion['numeracion']
    tipo = data_creacion['nombre']
    if not cursos.objects.filter(Nombre_curso=tipo,Numeracion_curso=numeracion).exists():
        curso_nuevo = cursos(Nombre_curso=tipo,Numeracion_curso=numeracion)
        curso_nuevo.save()
        return redirect('gestor')
    return redirect('gestor')

def eliminacion_curso(request,curso):
    delete_c = cursos.objects.get(Codigo_curso = curso)
    delete_c.delete()
    return redirect('gestor')

def modificar_curso(request,curso):
    data_modificacion = request.post
    return redirect('gestor')

#paralelos
def creacion_paralelo(request):
    return render(request, 'cursos/creacion_paralelo.html')

def generacion_paralelo(request):
    data_creacion = request.POST
    curso = data_creacion['curso']
    n_paralelo= data_creacion['numero_p']
    if not Paralelo.objects.filter(Numero_paralelo=n_paralelo,curso_paralelo_id=curso).exists():
        Paralelo_nuevo = Paralelo(Numero_paralelo=n_paralelo,curso_paralelo_id = curso)
        
        Paralelo_nuevo.save()
        return redirect('gestor')
    return redirect('gestor')

def eliminacion_paralelo(request,paralelo):
    delete_p = Paralelo.objects.get(codigo_paralelo = paralelo)
    delete_p.delete()
    return redirect('gestor')

@login_required
def cursos_home(request):
    
    data = {}
    if request.user.tipo == "Str":
        lista_curso = cursos.objects.all()
        data = {"cursos" : lista_curso}
        return render(request,"Core/cursos/cursos.html",data)
    if request.user.tipo == "Tea":
        lista_paralelos = Paralelo.objects.all()
        lista_curso = cursos.objects.all()
        data = {"paralelos" : lista_paralelos,"cursos_lista": lista_curso}
        return render(request,"Core/cursos/cursos.html",data)
    return redirect('inicio')

@login_required
def inicio(request):
    return render(request,"Core/inicio.html")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
<<<<<<< HEAD
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
=======
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
>>>>>>> cd6759f556e37cd4d39bc74157f901c56c2c9a88

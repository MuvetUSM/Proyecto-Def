from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import *
from .forms import RegistroUsuario, IniciarUsuario, EditCursoForm, CreateForo, CreateDiscussion


# Create your views here.

@login_required
def home(request):
    return render(request, 'Core/home.html')

def exit(request):
    logout(request)
    return redirect('home')

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

class CustomPasswordResetView(auth_views.PasswordResetView):
    form_class = PasswordResetForm
    email_template_name = 'egistration/password_reset_email.html'
    subject_template_name = 'egistration/password_reset_subject.txt'
    from_email = 'your_email@example.com'

    def get_users(self, correo):
        """Return a list of users that match the given correo."""
        return Usuario.objects.filter(correo__iexact=correo)

    def form_valid(self, form):
        opts = {
            'use_https': self.request.is_secure(),
            'email_template_name': self.email_template_name,
            'ubject_template_name': self.subject_template_name,
            'equest': self.request,
            'from_email': self.from_email,
            'html_email_template_name': 'registration/password_reset_email.html',
        }
        form.save(**opts, correo=form.cleaned_data['correo'])

        def get_users(self, correo):
            return Usuario.objects.filter(correo__iexact=correo)
        return super().form_valid(form)



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
        return redirect('Curso')
    return redirect('Curso')

def eliminacion_paralelo(request,paralelo):
    delete_p = Paralelo.objects.get(codigo_paralelo = paralelo)
    delete_p.delete()
    return redirect('Curso')

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
        return render(request, 'Core/cursos/cursos.html', data)
    return redirect('home')




#asignaturas
@login_required
def save_asignatura(request):
    curso_asignado = list(map(int, request.POST.getlist("curso_id")))
    paralelos_asignados = request.POST.getlist("paralelos_elegidos")
    asignatura_nombre = request.POST["nombre_asignatura"]
    asignatura_semestre = request.POST["semestre_elegido"]
    Asignatura_nueva = Asignaturas(Nombre_Asignatura = asignatura_nombre,semestre = asignatura_semestre)
    Asignatura_nueva.save()
    
    for x in curso_asignado: 
        
        Asignatura_nueva.curso_asociado.add(x)
    for x in paralelos_asignados:
        
        Asignatura_nueva.Asignatura_paralelo.add(x)
    return redirect('Asignatura')
@login_required
def asigantura_home(request):
    asiganturas_lista = Asignaturas.objects.all()
    cursos = Curso.objects.all()
    paralelos_a = Paralelo.objects.all()
    data = {"Asignaturas": asiganturas_lista,"Cursos": cursos,"Paralelos": paralelos_a}
    return render(request,'Core/asignaturas/asignatura.html',data)


#cursos y paralelos (mont)
@login_required
def Cursos_visualizacion(request):
    cursos = Curso.objects.all()
    Paralelos = Paralelo.objects.all()
    usuarios = Usuario.objects.filter(tipo = 'Tea')
    
    if 'tipo_educacion' in request.POST and 'nivel' in request.POST:
        #profesor_elegido = Usuario.objects.filter(correo = request.POST["profesor"])
        curso = Curso(nivel_educativo = request.POST["tipo_educacion"],grado = request.POST["nivel"])
        curso.save()
        
    

    return render(request, 'Core/cursos.html', {'cursos': cursos,'Paralelos': Paralelos,'Profesores': usuarios})

@login_required
def edicion_curso(request, codigo):
    curso = get_object_or_404(Curso, Codigo_curso=codigo)
    
    if request.method == 'POST':
        form = EditCursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('Curso') 
    else:
        form = EditCursoForm(instance=curso)
    
    return render(request, 'Core/edicion.html', {'form': form})

@login_required
def eliminar_curso(request, codigo):
    curso = get_object_or_404(Curso, Codigo_curso=codigo)
    curso.delete()
    return redirect('Curso') 

@login_required
def modificar_paralelo(request,paralelo):
    paralelo_elegido = Paralelo.objects.get(codigo_paralelo = paralelo)
    data =  {
        "paralelo": paralelo_elegido
    }
    #modificacion del paralelo
    if request.POST and not Paralelo.objects.filter(Numero_paralelo=request.POST["Numero_paralelo"],curso_paralelo=request.POST["curso"]).exists():
        Paralelo.objects.filter(codigo_paralelo=paralelo).update(Numero_paralelo=request.POST["Numero_paralelo"])
        return redirect('Curso')
    
    #direcciona a la pagina de modificacion
    return render(request,'Core/cursos/modificacion_paralelo.html',data)

#FORO
def foro(request):

    foros = Foro.objects.all()
    counts = len(foros)
    discussions = Discussion.objects.all()

    context = {
        'foros': foros,
        'counts': counts,
        'discussions': discussions
    }
    return render(request, 'Core/foro/foro.html', context)
    

def add_foro(request):
    form = CreateForo() 
    if request.method == 'POST':
        form = CreateForo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foro')
        
    context = {'form':form}
    return render(request, 'Core/foro/add_foro.html', context)
    

def add_discussion(request, foro_id):
    foro = Foro.objects.get(id=foro_id)
    form = CreateDiscussion()
    if request.method == 'POST':
        form = CreateDiscussion(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.foro = foro
            discussion.save()
            return redirect('foro')
        
    context = {'form': form, 'foro': foro}
    return render(request, 'Core/foro/add_discussion.html', context)

def delete_discussion(request, foro_id):
    foro = get_object_or_404(Foro, id=foro_id)
    foro.delete()
    return redirect('foro') 

#Post (loreto)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Core/post/post.html', {'posts': posts})

def post_delete(request):
    return 0

def post_edit(request):
    return 0



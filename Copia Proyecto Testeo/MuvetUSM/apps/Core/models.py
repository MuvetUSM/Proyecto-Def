from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.conf import settings
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, apellido, password=None):
        if not correo:
            raise ValueError('El Usuario debe asociar un correo.')

        usuario = self.model(
            nombre = nombre,
            apellido = apellido,
            correo=self.normalize_email(correo)
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, nombre, apellido, password):
        usuario = self.create_user(
            nombre = nombre,
            apellido = apellido,
            correo = self.normalize_email(correo),
            password=password
        )
        usuario.super = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    nombre = models.CharField('nombre', max_length=50, blank=False, null=False)
    apellido = models.CharField('apellido', max_length=50, blank=False, null=False)
    correo = models.EmailField('correo', max_length=254, unique=True, blank=False, null=False)
    fecha = models.DateField('fechaNacimiento', null=False, blank=False, default=timezone.now)
    username = models.CharField('username', max_length=100)
    tipo = models.CharField('Tipo', max_length=3, choices=[('Stu', 'Estudiante'), ('Tea', 'Profesor'), ('Str', 'Otro')])
    activo = models.BooleanField(default=True)
    super = models.BooleanField(default=False)
    # imagen = models.ImageField('Imagen', upload_to='usuarios/', null=True, blank=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre','apellido']

    def __str__(self):
        return f'{self.username}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"{self.nombre}{self.apellido}"
        super().save(*args, **kwargs)
    
    @property
    def is_staff(self):
        return self.super


    



#mont
#modelo correspondiente al curso
class Curso(models.Model):
    tipo_nivel_educativo = [("Basico","Basico"),("Medio","Medio")]
    grado = models.CharField(max_length=50, default=None)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    nivel_educativo =  models.CharField(choices=tipo_nivel_educativo,null=False,max_length=40)
    Codigo_curso = models.AutoField(primary_key=True)

    def __str__(self):
        return   self.grado + " " + self.nivel_educativo
class Paralelo(models.Model):
    codigo_paralelo = models.AutoField(primary_key=True)
    Numero_paralelo = models.IntegerField(null=False)
    curso_paralelo = models.ForeignKey(Curso,on_delete=models.CASCADE)
    def __str__(self):
        return f'Paralelo {self.Numero_paralelo} | Curso {self.curso_paralelo}'   

class Asignaturas(models.Model):
    codigo_asignatura = models.AutoField(primary_key=True)
    Nombre_Asignatura = models.CharField(max_length=50, default=None)
    curso_asociado = models.ManyToManyField(Curso)
    semestre = models.IntegerField(choices=[(1,"1 semestre"),(2,"2 semestre")])
    Asignatura_paralelo = models.ManyToManyField(Paralelo)
    def __str__(self) -> str:
        return f"{self.Nombre_Asignatura}"

#FORO
class Foro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tema = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=100, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.tema)
    

class Discussion(models.Model):
    hilo = models.ForeignKey(Foro, blank=True, on_delete=models.CASCADE)
    discusion = models.CharField(max_length=1000)

    def __str__(self):
        return self.hilo
    
#post (loreto)
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(max_length=20, choices=[
        ('entregable', 'Entregable'),
        ('contenido', 'Contenido'),
        ('comunicado', 'Comunicado'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
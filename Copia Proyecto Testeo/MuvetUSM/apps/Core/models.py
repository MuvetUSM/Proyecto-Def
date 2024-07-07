from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

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

class Asignatura(models.Model):
    name = models.CharField(max_length=200)
    grado = models.CharField(max_length=50, default=None)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name



#mont
tipo_nivel_educativo = [("BA","Basico"),("ME","Medio")]

#modelo correspondiente al curso
class cursos(models.Model):
    Numeracion_curso = models.IntegerField(null=True)
    Nombre_curso = models.CharField(choices=tipo_nivel_educativo,null=False,max_length=40)
    Codigo_curso = models.AutoField(primary_key=True)
    
    
    def __str__(self) -> str:
        nombre_curso = ""
        for x in tipo_nivel_educativo:
            if self.Nombre_curso in x:
                nombre_curso = x[1]
        return f"{self.Numeracion_curso} {nombre_curso}"

class Paralelo(models.Model):
    codigo_paralelo = models.AutoField(primary_key=True)
    Numero_paralelo = models.IntegerField(null=False)
    curso_paralelo = models.ForeignKey(cursos,on_delete=models.CASCADE)
    def __str__(self):
        return f'Paralelo {self.Numero_paralelo} | Curso {self.curso_paralelo}'   

from django import forms
from django.forms import ModelForm
from .models import *

class RegistroUsuario(forms.ModelForm):
    Password1 = forms.CharField(label = "Contraseña.", widget= forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Ingresar Contraseña...',
            'id': 'Pass1',
            'required': 'required',
        }
    ))
    Password2 = forms.CharField(label = "Confirmar Contraseña.", widget= forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Reingresar Contraseña...',
            'id': 'Pass2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'correo', 'fecha')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Apellido'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Email'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Fecha de nacimiento'}),
        }

class IniciarUsuario(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('correo',)


class CreateNewCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [ 'grado', 'usuario']
        widgets = {
            'grado': forms.TextInput(attrs={'class': 'input'}),
            'usuario': forms.Select(attrs={'class': 'input'}),
        }

class EditCursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [ 'grado', 'usuario']
        widgets = {
            'grado': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
        
#FORO
class CreateForo(ModelForm):
    class Meta:
        model = Foro
        fields = "__all__"

class CreateDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"

class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('name', 'descripcion', 'comunicado', 'entregable', 'archivo')

    def __init__(self, *args, **kwargs):
        super(postForm, self).__init__(*args, **kwargs)
        self.fields['archivo'].widget.attrs.update({'accept': '.png, .pdf, .csv, .docx'})

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        if archivo:
            if archivo.size > 1024 * 1024 * 5:  # 5MB
                raise forms.ValidationError('El archivo es demasiado grande. Debe ser menor a 5MB.')
            return archivo
        return None

class repositorioForm(forms.ModelForm):
    class Meta:
        model = repositorio
        fields = ('name', 'descripcion')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Nombre del repositorio'
        self.fields['descripcion'].label = 'Descripción del repositorio'
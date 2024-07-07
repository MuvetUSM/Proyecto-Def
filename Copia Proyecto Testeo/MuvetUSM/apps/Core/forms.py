from django import forms
from .models import Usuario, Asignatura

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
        model = Asignatura
        fields = ['name', 'grado', 'usuario']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'grado': forms.TextInput(attrs={'class': 'input'}),
            'usuario': forms.Select(attrs={'class': 'input'}),
        }

class EditCursoForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['name', 'grado', 'usuario']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'grado': forms.TextInput(attrs={'class': 'input'}),
            'usuario': forms.Select(attrs={'class': 'input'}),
        }


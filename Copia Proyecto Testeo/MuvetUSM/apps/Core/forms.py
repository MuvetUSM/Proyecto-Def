from django import forms
from apps.Core.models import Usuario

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
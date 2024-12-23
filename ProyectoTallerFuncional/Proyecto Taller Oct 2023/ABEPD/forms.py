from django import forms
from .models import Empresa

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Empresa
        fields = ['username', 'nombre_empresa', 'rut_empresa', 'correo_empresa', 'telefono_contacto', 'direccion_empresa', 'tipo_industria','password']

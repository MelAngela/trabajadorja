from django import forms
from .models import Trabajador, Cargas

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['rut', 'apellido_paterno', 'apellido_materno', 'nombres', 'fecha_nacimiento', 'sexo', 'estado_civil']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


class CargasForm(forms.ModelForm):
    class Meta:
        model = Cargas
        fields = ['trabajador', 'apellido_paterno', 'apellido_materno', 'nombre', 'fecha_nacimiento', 'sexo', 'parentesco']
        widgets = {
            # 'trabajador': forms.HiddenInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


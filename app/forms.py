from django import forms
from .models import Solicitud 

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'nombre_usuario',
            'apellido_usuario',
            'rut',
            'email',
            'numero_telefono',
            'servicio',
            'tipo_consulta',
            'descripcion',
        ]
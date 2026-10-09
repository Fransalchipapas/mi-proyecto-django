from django import forms
from .models import Curso
class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso # Vinculación explícita con el modelo físico
        fields = ['nombre', 'camada'] # Columnas expuestas en la interfaz
        # Sobreescritura visual y adición de clases de diseño (Bootstrap)
        labels = {
            'nombre': 'Nombre del Curso',
            'camada': 'Número de Camada'
        }
        widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'camada': forms.NumberInput(attrs={'class': 'form-control'}),
        }
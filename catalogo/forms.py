from django import forms
from .models import Videojuego


class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'plataforma', 'precio', 'fecha_lanzamiento', 'disponible']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'plataforma': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_lanzamiento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

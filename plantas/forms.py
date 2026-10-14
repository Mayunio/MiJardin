from django import forms
from .models import Planta

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        if len(nombre) < 3:
            raise forms.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
            )

        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']

        if len(descripcion) < 10:
            raise forms.ValidationError(
                'La descripción debe tener al menos 10 caracteres.'
            )

        return descripcion

    
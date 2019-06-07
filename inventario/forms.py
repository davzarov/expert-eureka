from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    # imagen = forms.FileField(widget=forms.FileInput())

    class Meta:
        model = Producto
        fields = (
            'nombre',
            # 'imagen',
            'descripcion',
            'cantidad',
            'precio_costo',
            'disponible'
        )

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget = forms.TextInput(attrs={})
        self.fields['descripcion'].required = False
        self.fields['descripcion'].widget = forms.Textarea(attrs={
            'class': 'materialize-textarea'
        })
        self.fields['precio_costo'].widget = forms.NumberInput(attrs={})
        self.fields['cantidad'].widget = forms.NumberInput(attrs={})
        self.fields['disponible'].widget = forms.CheckboxInput(attrs={})

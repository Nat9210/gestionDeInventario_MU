from django import forms
from .models import MovimientoStock
from inventario.models import Pieza


class MovimientoForm(forms.ModelForm):
    """Formulario para registrar movimientos de stock"""
    
    class Meta:
        model = MovimientoStock
        fields = ('pieza', 'cantidad', 'observaciones')
        labels = {
            'pieza': 'Seleccionar pieza',
            'cantidad': 'Cantidad',
            'observaciones': 'Observaciones (opcional)'
        }
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        tipo_movimiento = kwargs.pop('tipo_movimiento', None)
        super().__init__(*args, **kwargs)
        
        # Aplicar clases CSS
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Configurar campo de cantidad
        self.fields['cantidad'].widget.attrs.update({
            'min': '1',
            'placeholder': 'Ingrese la cantidad'
        })
        
        # Configurar campo de pieza
        self.fields['pieza'].queryset = Pieza.objects.all().order_by('codigo')
        self.fields['pieza'].widget.attrs.update({'id': 'pieza-select'})
        
        # Personalizar según tipo de movimiento
        if tipo_movimiento == 'entrada':
            self.fields['observaciones'].widget.attrs.update({
                'placeholder': 'Ej: Compra, devolución, ajuste de inventario...'
            })
        elif tipo_movimiento == 'salida':
            self.fields['observaciones'].widget.attrs.update({
                'placeholder': 'Ej: Uso en proyecto, mantenimiento, ajuste...'
            })
    
    def clean_cantidad(self):
        """Validar que la cantidad sea positiva"""
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad <= 0:
            raise forms.ValidationError('La cantidad debe ser mayor a 0.')
        return cantidad

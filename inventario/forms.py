from django import forms
from .models import Pieza


class PiezaForm(forms.ModelForm):
    """Formulario para crear y editar piezas"""
    
    class Meta:
        model = Pieza
        fields = ('codigo', 'descripcion', 'stock_actual', 'stock_minimo', 'ubicacion', 'categoria')
        labels = {
            'codigo': 'Código de la pieza',
            'descripcion': 'Descripción',
            'stock_actual': 'Stock actual',
            'stock_minimo': 'Stock mínimo',
            'ubicacion': 'Ubicación en bodega',
            'categoria': 'Categoría'
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Validaciones adicionales
        self.fields['codigo'].widget.attrs.update({'placeholder': 'Ej: P001'})
        self.fields['stock_actual'].widget.attrs.update({'min': '0'})
        self.fields['stock_minimo'].widget.attrs.update({'min': '1'})
    
    def clean_codigo(self):
        """Validar que el código sea único"""
        codigo = self.cleaned_data.get('codigo', '').upper()
        
        # Si estamos editando, excluir la instancia actual
        if self.instance.pk:
            if Pieza.objects.exclude(pk=self.instance.pk).filter(codigo=codigo).exists():
                raise forms.ValidationError('Ya existe una pieza con este código.')
        else:
            if Pieza.objects.filter(codigo=codigo).exists():
                raise forms.ValidationError('Ya existe una pieza con este código.')
        
        return codigo
    
    def clean(self):
        """Validaciones generales"""
        cleaned_data = super().clean()
        stock_actual = cleaned_data.get('stock_actual')
        stock_minimo = cleaned_data.get('stock_minimo')
        
        if stock_actual is not None and stock_minimo is not None:
            if stock_minimo <= 0:
                raise forms.ValidationError('El stock mínimo debe ser mayor a 0.')
        
        return cleaned_data

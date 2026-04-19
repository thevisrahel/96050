from django import forms

class FormularioProducto(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea)
    
    
class FormularioBusqueda(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    

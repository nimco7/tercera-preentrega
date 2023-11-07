from django import forms

class CrearProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    
class BusquedaProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    
    
class CrearCategoriaFormulario(forms.Form):
    categoria = forms.CharField(max_length=30)
    
    
class CrearReseniaFormulario(forms.Form):
    resenia = forms.CharField(max_length=250)
    
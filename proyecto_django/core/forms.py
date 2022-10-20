from django import forms
from .models import Producto
class AgregarProducto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    precio = forms.FloatField(label="Precio") 
    cantidad = forms.IntegerField(label="Cantidad")
    fecha_ingreso = forms.DateField(label= "Fecha ingreso",input_formats=["%d/%m/%Y"])


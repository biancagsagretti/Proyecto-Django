from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import forms

# Create your views here.

def index(request):
    contexto = {
        'encabezado_1':"Inventario Django",
        
        'productos': [
        ("Bananas"),
        ("Peras")
]

    }
    print(reverse("acerca_de"))
    print(reverse("landing"))

    return render(request, 'core/index.html',contexto)

def acerca_de(request):
    
    contexto = {
        'encabezado_1': 'Acerca de nosotros',
    }

    return  render(request,'core/acerca_de.html', contexto)
    

def landing_page(request):
    html = """
     <style>
            body {
                background-color: red;
            }

            h1, p {
                text-align: center;
                color: white;
            }
        </style>
        <header>
            <h1>Landing page del Aula Virtual 1.0</h1>
        </header>
        <main>
            <p>Bienvenid@s al aula virtual Django 1.0</p>
        </main>
        <footer>
            <p>Todos los derechos reservados. Digit@lers 2022.</p>
        </footer>
    """
    
    return HttpResponse(html)

def agregar_producto(request):
    if request.method == "POST":
        form = forms.AgregarProducto(request.POST)
    if form.is_valid():
        print(form.cleaned_data['nombre'])
        print(form.cleaned_data['precio'])
        print(form.cleaned_data['cantidad'])
        print(form.cleaned_data['fecha_ingreso'])
        return HttpResponseRedirect(reverse("index"))

    else:
        form = forms.AgregarProducto()
    ctx = {
        "encabezado_1": "Agregar Alumno al sistema",
        "formulario": form
        }
    return render(request, "core/agregar_producto.html", ctx)
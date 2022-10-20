from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import forms
from. import models


# Create your views here.

def index(request):
    productos = models.Producto.objects.all()
    contexto = {
        'encabezado_1':"Inventario Django",
        'productos': productos        
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
                background-color:rgb(201, 146, 201);
            }

            h1, p {
                text-align: center;
                color: white;
            }
        </style>
        <header>
            <h1>Landing page del Inventario</h1>
        </header>
        <main>
            <p>Bienvenidos al Inventario Django</p>
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
            nuevo_producto = models.Producto(
            nombre = form.cleaned_data['nombre'],
            precio= form.cleaned_data['precio'],
            cantidad= form.cleaned_data['cantidad'],
            fecha_ingreso= form.cleaned_data['fecha_ingreso'],
           
            )
            nuevo_producto.save()
        return HttpResponseRedirect(reverse("index"))

    else:
        form = forms.AgregarProducto()
    ctx = {
        "encabezado_1": "Agregar Producto al sistema",
        "formulario": form
        }
    return render(request, "core/agregar_producto.html", ctx)

def listar_producto (request):
    productos= models.Producto.objects.all()
    return render(request, "core/listar_producto.html", {"productos": productos})

def editar_producto(request, slug):
    producto = models.Producto.objects.get(slug=slug)

    nombre = request.POST.get('nombreInput')
    precio = request.POST.get('precioInput')
    cantidad = request.POST.get('cantidadInput')
    fecha_ingreso = request.POST.get('fecha_ingresoInput')
    if request.method == 'POST':

        producto.nombre = nombre
        producto.precio = precio
        producto.cantidad = cantidad
        producto.fecha_ingreso = fecha_ingreso
        producto.save()
        
        return redirect('/')

    return render (request, "core/editar_producto.html", {"producto": producto})

def borrar_producto(request, slug):
    producto = models.Producto.objects.get(slug=slug)

    producto.delete()
   
    return redirect('/')  






        
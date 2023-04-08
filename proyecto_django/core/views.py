from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import forms
from. import models



# Create your views here.

def index(request):
    productos = models.Producto.objects.all()
    contexto = {
        'encabezado_1':"Inventario Django",
             
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
        return HttpResponseRedirect(reverse("listar_productos"))

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

def editar_producto(request):
    productos= models.Producto.objects.all()
    
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
        return HttpResponseRedirect(reverse("listar_productos"))

    else:
        form = forms.AgregarProducto()
    ctx = {
        "encabezado_1": "Agregar Producto al sistema",
        "formulario": form,
        "productos": productos
        }
   


    return render (request, "core/editar_producto.html", ctx)

def borrar_producto(request, id):
        

    productos = get_object_or_404(models.Producto, id =id)
    productos.delete()
    return HttpResponseRedirect(reverse("listar_productos"))





        
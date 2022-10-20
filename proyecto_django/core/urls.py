from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca_de', views.acerca_de, name='acerca_de'),
    path('landing', views.landing_page, name="landing"),
    path("agregar_productos", views.agregar_producto, name="agregar_productos"),
    path("borrar_productos", views.borrar_producto, name="borrar_productos"),
    path("editar_productos", views.editar_producto, name="editar_productos"),
    path("listar_productos", views.listar_producto, name="listar_productos")
   

]
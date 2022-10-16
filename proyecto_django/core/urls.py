from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca_de', views.acerca_de, name='acerca_de'),
    path('landing', views.landing_page, name="landing"),
    path("agregar_producto", views.agregar_producto, name="agregar_producto")

]
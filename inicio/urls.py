
from django.urls import path
from inicio.views import inicio, crear_libro, listado_de_libros

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("libros/crear/", crear_libro, name="crear_libro"),
    path("libros/", listado_de_libros, name="listado_de_libros"),
]
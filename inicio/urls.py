
from django.urls import path
from inicio.views import inicio, crear_libro, listado_de_libros, libro_detalle, LibroBorrar, LibroActualizar

urlpatterns = [
    path("", inicio, name="inicio"),
    path("libros/crear/", crear_libro, name="crear_libro"),
    path("libros/", listado_de_libros, name="listado_de_libros"),
    path("libros/<int:id_libro>", libro_detalle, name="libro_detalle"),
    path("libros/<int:pk>/borrar/", LibroBorrar.as_view(), name="libro_borrar"),
    path("libros/<int:pk>/actualizar/", LibroActualizar.as_view(), name="libro_actualizar"),
]
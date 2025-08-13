
from django.urls import path
from inicio.views import inicio, crear_auto, listado_de_autos

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("autos/crear/", crear_auto, name="crear_auto"),
    path("autos/", listado_de_autos, name="listado_de_autos"),
]
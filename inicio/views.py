from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Libro
from inicio.forms import FormularioCrearLibro, FormularioBuscarLibro
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
#En el htpp response están las respuestas que se devuelven a los request. Por eso se importan y se usan en el return de abajo, devuelve la respuesta

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")


def crear_libro(request):

    print(request.POST)

    if request.method == "POST":
        formulario = FormularioCrearLibro(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            libro = Libro(titulo=info.get("titulo"), autor=info.get("autor"))
            libro.save()

            return redirect("listado_de_libros")
    else:
        formulario = FormularioCrearLibro()
        
    return render(request, "crear_libro.html", {"formulario": formulario})

def listado_de_libros(request):

    formulario = FormularioBuscarLibro(request.GET)
    if formulario.is_valid():
        titulo_a_buscar = formulario.cleaned_data["titulo"]
        libros_buscados = Libro.objects.filter(titulo__icontains=titulo_a_buscar)

    else:
        libros_buscados = Libro.objects.all()
    
    return render(request, "listado_de_libros.html", {"libros_buscados": libros_buscados, "formulario": formulario})

def libro_detalle(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    return render(request, "libro_detalle.html", {"libro": libro})

#def libro_borrado(request, id_libro):
 #   libro = Libro.objects.get(id=id_libro)
  #  libro.delete()
   # return render(request, "libro_detalle.html", {"libro": libro})

class LibroBorrar(DeleteView):
    model = Libro
    template_name = 'libro_borrar.html'
    success_url = reverse_lazy("listado_de_libros")


class LibroActualizar(UpdateView):
    model = Libro
    template_name = 'libro_actualizar.html'
    success_url = reverse_lazy("listado_de_libros")
    fields = ["titulo", "autor"]

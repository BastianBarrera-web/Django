from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Libro
from inicio.forms import FormularioCrearLibro
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

    libros = Libro.objects.all()
    
    return render(request, "listado_de_libros.html", {"libros": libros})

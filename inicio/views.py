from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Auto
from inicio.forms import FormularioCrearAuto
#En el htpp response están las respuestas que se devuelven a los request. Por eso se importan y se usan en el return de abajo, devuelve la respuesta

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")


def crear_auto(request):

    print(request.POST)

    if request.method == "POST":
        formulario = FormularioCrearAuto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            auto = Auto(marca=info.get("marca"), modelo=info.get("modelo"))
            auto.save()

            return redirect("listado_de_autos")
    else:
        formulario = FormularioCrearAuto()
        
    return render(request, "crear_auto.html", {"formulario": formulario})

def listado_de_autos(request):

    autos = Auto.objects.all()
    
    return render(request, "listado_de_autos.html", {"autos": autos})
    
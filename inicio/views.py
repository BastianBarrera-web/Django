from django.shortcuts import render
from django.http import HttpResponse
#En el htpp response están las respuestas que se devuelven a los request. Por eso se importan y se usan en el return de abajo, devuelve la respuesta

# Create your views here.

def inicio(request):
    return HttpResponse ("Esta es la página de inicio")
    
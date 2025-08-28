from django import forms

class FormularioCrearLibro(forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=30)
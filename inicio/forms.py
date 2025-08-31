from django import forms


class FormularioBaseLibro(forms.Form):
    titulo = forms.CharField(max_length=50)
    

class FormularioCrearLibro(FormularioBaseLibro):
    autor = forms.CharField(max_length=30)


class FormularioBuscarLibro(FormularioBaseLibro):
    titulo = forms.CharField(max_length=50, required=False)
    autor = forms.CharField(max_length=30, required=False)

from django import forms

class LibroFormulario(forms.Form):

    genero = forms.CharField()
    titulo = forms.CharField()
    numero_de_guia = forms.IntegerField()
    sinopsis = forms.CharField(widget=forms.Textarea)

class SocioFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()

class JuegoFormulario(forms.Form):

    titulo = forms.CharField()
    numero_de_guia = forms.IntegerField()
    precio = forms.IntegerField()


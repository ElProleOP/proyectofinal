from django.shortcuts import render , HttpResponse
from django.http import HttpResponse
from AppEntrega.forms import LibroFormulario, SocioFormulario, JuegoFormulario
from AppEntrega.models import Libros, Socio , Juegomesa, Avatar


# Create your views here.

def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "AppEntrega/inicio.html" , {"url": avatares[0].imagen.url})

def librosFormulario(request):

      if request.method == 'POST':
            
            miformulario = LibroFormulario(request.POST)

            print(miformulario)
            
            if miformulario.is_valid:

                  informacion = miformulario.cleaned_data

                  libro = Libros(genero=informacion['genero'], titulo = informacion['titulo'], 
                  numero_de_guia = informacion ['numero_de_guia'], sinopsis = informacion['sinopsis'])

                  libro.save()

                  return render(request, "AppEntrega/libross.html")
      else:

            miformulario = LibroFormulario()

      return render(request, "AppEntrega/librosFormulario.html", {"miFormulario":miformulario})

def sociosFormulario(request):

      if request.method == 'POST':
            
            miformulario2 = SocioFormulario(request.POST)

            
            if miformulario2.is_valid:

                  informacion2 = miformulario2.cleaned_data

                  socio = Socio(nombre=informacion2['nombre'], apellido = informacion2['apellido'],
                   edad = informacion2 ['edad'], email = informacion2 ['email'])

                  socio.save()

                  return render(request, "AppEntrega/inicio.html")
      else:

            miformulario2 = SocioFormulario()

      return render(request, "AppEntrega/sociosFormulario.html", {"miFormulario2":miformulario2})

def busquedaSocio(request):

      return render(request, 'AppEntrega/busquedaSocio.html')

def buscar(request):

      if request.method == "GET":

           email = request.GET['email']

           socios = Socio.objects.filter(email__icontains = email)

           return render(request, 'AppEntrega/resultadoBusqueda.html', {'socios':socios , 'email':email})

      else:
            respuesta = "No enviaste nada"
      return HttpResponse (respuesta)

def juegosFormulario(request):

      if request.method == 'POST':
            
            miformulario3 = JuegoFormulario(request.POST)

            print(miformulario3)
            
            if miformulario3.is_valid:

                  informacion3 = miformulario3.cleaned_data

                  juego = Juegomesa(titulo=informacion3['titulo'],
                   numero_de_guia = informacion3 ['numero_de_guia'], precio = informacion3 ['precio'])

                  juego.save()

                  return render(request, "AppEntrega/inicio.html")
      else:

            miformulario3 = JuegoFormulario()

      return render(request, "AppEntrega/juegosFormulario.html", {"miFormulario3":miformulario3})


def leerlibros(request):

      libros = Libros.objects.all()
      contexto = {'libros': libros}
      return render(request, 'AppEntrega/leerlibros.html', contexto)

def eliminarlibro(request,numero_guia):

      libro = Libros.objects.get(numero_de_guia = numero_guia)
      libro.delete()

      libros = Libros.objects.all()
      contexto = {'libros': libros}
      return render(request, 'AppEntrega/leerlibros.html', contexto)

def verlibro(request, numero_guia):

      libro=Libros.objects.get(numero_de_guia=numero_guia)
      contexto = {'libro': libro}
      return render(request,'AppEntrega/librodetalles.html', contexto)

def about(request):
      return render(request, 'AppEntrega/about.html')


      


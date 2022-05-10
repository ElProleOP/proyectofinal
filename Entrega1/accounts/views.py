from collections import UserList, UserString
from django.shortcuts import render
from accounts.forms import UserRegisterForm, UserEditForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_request(request):

    if request.method == "POST":

            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():

                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
        
                  if user is not None:
                        login(request, user)

                        return render (request, "AppEntrega/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        
                        return render (request, "AppEntrega/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "AppEntrega/inicio.html", {"mensaje":"Formulario erroneo"})
      

    form = AuthenticationForm()
  
    return render(request, "accounts/login.html", {'form': form})


def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():

                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "accounts/registers.html", {"mensaje": "Usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "accounts/register.html", {"form": form})

@login_required
def editarPerfil(request):
 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario4 = UserEditForm(request.POST)
            if miFormulario4.is_valid: 
                  informacion = miFormulario4.cleaned_data

                  usuario.first_name = informacion['nombre']
                  usuario.last_name = informacion['apellido']
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppEntrega/inicio.html") 

      else:
            miFormulario4 = UserEditForm(initial={'email':usuario.email})
      
      return render(request, "accounts/editarperf.html", {"miFormulario4": miFormulario4, "usuario": usuario})


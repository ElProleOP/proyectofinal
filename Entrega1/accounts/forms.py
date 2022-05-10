from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User                                            
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {'username': 'Nombre de usuario', 'email':'Email','last_name': 'Apellido', 'first_name':'Nombre'}
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 

    nombre = forms.CharField(label= 'modificar nombre')
    apellido = forms.CharField(label= 'modificar apellido')
    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['nombre','apellido','email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}
from django.urls import path
from AppEntrega import views

urlpatterns = [

    path('', views.inicio ,  name='inicio'),
    path('libros/' , views.librosFormulario , name='Libros'),
    path('socios/' , views.sociosFormulario, name = 'Socios'),
    path('busquedaSocio/', views.busquedaSocio, name ='BusquedaSocio'),
    path('AppEntrega/buscar/', views.buscar ),
    path('juegodemesa/', views.juegosFormulario , name= 'Juegomesa'),
    path('libroslist/', views.leerlibros, name = 'Librosl'),
    path('eliminarlibro/<numero_guia>/', views.eliminarlibro , name="Eliminar"),
    path('about/', views.about, name= 'about'),
    path('detalles/<numero_guia>/', views.verlibro, name = 'Detalles')
]
from django.urls import path
from . import views

urlpatterns = [
    path('lista_contactos/', views.ListaContactos, name='contactos'),
    path('', views.Lista, name='lista'),
    path('crear/', views.Crear, name='crear'), # registrar contacto con potsman
    path('contactos/', views.Listas, name='contactos'),
    path('nuevo_contacto/', views.crear_contacto, name='nuevo_contacto'),
    path('contactos_lista/', views.lista_contactos, name='contactos_lista'),
]
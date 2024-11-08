from django.shortcuts import render
from .models import Contactos
from .forms import ContactosForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def lista_contactos(request):
    contactos = Contactos.objects.all()  
    return render(request, 'contactos/mostrar_contactos.html', {"contactos": contactos})

def crear_contacto(request):
    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponse("El contacto se creo correctamente.")
    else:
        form = ContactosForm()
    return render(request, 'contactos/crear_contacto.html', {'form': form})



@csrf_exempt
def Crear(request):
     if request.method == 'POST':
        
        body = request.body.decode('utf-8')
        request_body = json.loads(body)   
        
        contacto = Contactos.objects.create(
            nombre = request_body['nombre'],
            telefono = request_body['telefono'],
            celular = request_body['celular'],
            correo = request_body['correo'],
            direccion = request_body['direccion'],
            nacimiento = request_body['cumpleaños']
        )
        
        return JsonResponse(data={'message': 'El contacto a sido creado',
                                  'Nombre': contacto.nombre,
                                  'Celular': contacto.celular,
                                  'Correo': contacto.correo,
                                  'Direccion': contacto.direccion})
def Listas(request):
    if request.method == "GET":
        contactos = list(Contactos.objects.all().values("nombre",
                                                        "telefono",
                                                        "celular",
                                                        "correo",
                                                        "direccion",
                                                        "nacimiento"))

        return JsonResponse(data={"message": "Estos son tus contactos", "Contactos": contactos})
     
def ListaContactos(request):
    return HttpResponse("Bienvenido a tu pagina de Contactos.")

def Lista(request):
    return render(request, 'contactos/Contactos.html')
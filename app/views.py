from urllib.request import Request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SolicitudForm



# Create your views here.

def index(request):
    return render (request ,'app/index.html')

def internet(request):
    return render(request, 'app/internet.html')


def movil(request):
    return render(request, 'app/movil.html')

def telefonia(request):
    return render(request, 'app/telefija.html')

def registro(request):
    return render (request, 'app/registro.html')

def Solicitud(request):
    data = { 
        'form':SolicitudForm()
    }
    if request.method == 'POST':
        formulario = SolicitudForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return render( request, 'app/registro.html')
        else:
            data['form']= formulario
    return render(request, 'app/formulario.html', data)
    

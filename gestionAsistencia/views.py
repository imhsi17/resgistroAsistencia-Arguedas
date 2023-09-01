from django.shortcuts import render
from django.http import HttpResponse
from gestionAsistencia.models import Alumnos, Atrasado, Puntual

# Create your views here.

def inicio_sesion(request):
    return render(request, "index.html")

def verificacion(request):
    
    usuario = request.POST["dni"]
    contra = request.POST["psswrd"]
    almn = Alumnos.objects.filter(DNI__icontains=usuario)
    llegada_puntual = Puntual.objects.filter(DNI__icontains=usuario)    
    llegada_tarde = Atrasado.objects.filter(DNI__icontains=usuario)
    
    contexto = {"alumno":almn, "contraseña":contra, "atrasados":llegada_tarde, "puntuales":llegada_puntual,"query":usuario}
    return render(request, "vista_asistencia.html", contexto)
    

    

from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    about=About.objects.all() # Consulta para obtener todos los servicios
    return render(request,"about/about.html",{'listAbout':about})
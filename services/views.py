from django.shortcuts import render
from .models import Service, Testimonial

# Create your views here.
def services(request):
    services=Service.objects.all() # Consulta para obtener todos los servicios
    testimonials=Testimonial.objects.all()
    return render(request,"services/services.html",{'listServices':services,'listTestimonial':testimonials})
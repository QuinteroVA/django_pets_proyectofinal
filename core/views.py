from django.shortcuts import render

from services.models import Service
# Create your views here.
def home(request):
    return render(request,"core/home.html")
    
def blog(request):
    return render(request,"core/blog.html")
    
def single(request):
    return render(request,"core/single.html")

def booking(request):
    services=Service.objects.all()[:4]
    return render(request,"core/booking.html",{'listServices':services})
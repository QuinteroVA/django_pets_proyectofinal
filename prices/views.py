from django.shortcuts import render
from .models import Price, Plan

# Create your views here.
def prices(request):
    prices=Price.objects.all()
    plans=Plan.objects.all()
    return render(request,"prices/prices.html",{'listPrices':prices, 'listPlans':plans})
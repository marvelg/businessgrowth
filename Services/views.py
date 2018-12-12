from django.shortcuts import render
from .models import Slider
from .models import Service
# Create your views here.
def services(request):
    slider = Slider.objects
    service = Service.objects
    return render(request, 'Services/Services.html', {"Slider": slider, "Service" : service})

def product(request):
    return render(request, 'Services/Product.html')

def productdescription(request):
    return render(request, 'Services/Product-Description.html')